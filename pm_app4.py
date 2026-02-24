import streamlit as st
import pandas as pd
import google.generativeai as genai

st.title("📊 Live Jira Dashboard")

# 1. Load the Data
# In Java 2, this was 50 lines of IO code. In Python, it's one.
# try:
#    df = pd.read_csv("jira_export.csv")
# except FileNotFoundError:
#    st.error("CSV file not found! Please make sure 'jira_export.csv' is in the folder.")
#    st.stop()

# 1. Replace pd.read_csv('jira_export.csv') with this:
uploaded_file = st.file_uploader("Upload your Jira Export (CSV)", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    # The rest of your app logic goes here...
else:
    st.info("👆 Please upload a CSV file to begin.")
    st.stop()  # Stops the script until a file is provided

# 2. Sidebar: Project Selector
# We use the 'Issue Key' column from our CSV to fill a dropdown
st.sidebar.header("Filter Settings")
selected_issue = st.sidebar.selectbox("Select an Issue to Analyze", df["Issue Key"])

# 3. "Join" the UI to the Data
# We pull the specific row for the selected issue
issue_data = df[df["Issue Key"] == selected_issue].iloc[0]

# --- UI Display ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Issue Details")
    st.write(f"**Summary:** {issue_data['Summary']}")
    st.write(f"**Current Status:** {issue_data['Status']}")

with col2:
    # Use the Story Points from the CSV as the default slider value
    points = st.slider("Adjust Story Points", 1, 20, int(issue_data["Story Points"]))
    priority = st.text_input("Priority Level", value=issue_data["Priority"])

# 4. Data Visualization
st.divider()
st.subheader("Full Dataset")
# This creates an interactive, searchable table automatically
st.dataframe(df, use_container_width=True)

# 5. Quick Analytics
done_count = len(df[df["Status"] == "Done"])
st.info(f"Progress Check: {done_count} out of {len(df)} tasks are completed.")

# --- AI Configuration ---
# Replace 'YOUR_API_KEY' with the key you just got
# genai.configure(api_key="AIzaSyBA_xv5inXm3rhIQqOG1kxHVimvJVf9Cu4")

# Modern Python way: Get the key from the cloud environment

# This will look for a secret named 'GEMINI_API_KEY'
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

st.divider()
st.header("✉️ AI Status Report Generator")

if st.button("Generate Stakeholder Email"):
    # We pull the summary from the issue you selected in the previous step
    issue_summary = issue_data["Summary"]

    # This is "Prompt Engineering" - think of it as a highly descriptive method call
    prompt = f"""
    You are a professional Project Manager. 
    Write a short, concise status update email for the following task: "{issue_summary}".
    The task status is "{issue_data["Status"]}" and priority is "{issue_data["Priority"]}".
    Tone: Professional but urgent if high priority.
    """

    with st.spinner("Writing email..."):
        try:
            response = model.generate_content(prompt)
            email_draft = response.text  # Store the text in a variable

            # Show the result in the UI
            st.subheader("Draft Email:")
            st.info(email_draft)

            # --- THE DOWNLOAD MAGIC ---
            # This creates a 'Virtual File' in the user's browser
            st.download_button(
                label="💾 Download Email as .txt",
                data=email_draft,
                file_name=f"status_report_{selected_issue}.txt",
                mime="text/plain",
            )

        except Exception as e:
            st.error(f"AI Error: {e}")
