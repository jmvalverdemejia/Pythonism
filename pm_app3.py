import streamlit as st
import pandas as pd
import google.generativeai as genai

# --- 1. Cloud Secrets Setup ---_
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("📊 Universal Jira Dashboard")

# --- 2. The Dynamic File Uploader ---
# This replaces the hardcoded 'jira_export.csv'
uploaded_file = st.file_uploader("Upload your Jira Export (CSV)", type="csv")

if uploaded_file is not None:
    # If a user drops a file, we read it into memory
    df = pd.read_csv(uploaded_file)

    st.success("File loaded successfully!")

    # --- 3. Sidebar Selection ---
    # We use the 'Issue Key' column to fill the dropdown
    selected_issue = st.sidebar.selectbox("Select an Issue", df["Issue Key"])
    issue_data = df[df["Issue Key"] == selected_issue].iloc[0]

    # --- 4. Dashboard Logic (The rest of your code) ---
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Issue Details")
        st.write(f"**Summary:** {issue_data['Summary']}")
        st.write(f"**Status:** {issue_data['Status']}")

    with col2:
        # Use the data from the CSV as the default
        points = st.slider(
            "Adjust Story Points", 1, 20, int(issue_data["Story Points"])
        )
        priority = st.text_input("Priority", value=issue_data["Priority"])

    # --- 5. The AI Feature ---
    st.divider()
    if st.button("Generate Stakeholder Email"):
        prompt = f"""
You are a Senior Project Manager. Write a professional status update email.
Task: {issue_data["Summary"]}
Status: {issue_data["Status"]}
Priority: {issue_data["Priority"]}

Formatting Instructions:
1. Use a clear **Subject Line**.
2. Use ## for the main heading.
3. Use **bolding** for critical dates or names.
4. Use bullet points for "Next Steps".
5. Keep the tone professional yet approachable.
"""
        with st.spinner("AI is drafting..."):
            response = model.generate_content(prompt)
            email_draft = response.text

            # --- REFINED OUTPUT DISPLAY ---
            st.subheader("Final Draft Review")

            # We use a container with a border to make it look like a 'document'
            with st.container(border=True):
                st.markdown(email_draft)  # This renders the bold, headers, and lists
                st.toast("Email Drafted Successfully!", icon="✉️")
                st.balloons()  # Use this sparingly, but it's fun for the first time!

            # Move the download button below the preview
            st.download_button(
                label="💾 Download as Text File",
                data=email_draft,
                file_name=f"Update_{selected_issue}.txt",
                mime="text/plain",
            )

else:
    # This part runs if NO file is uploaded
    st.warning("Welcome, PM! Please upload a CSV export to begin your analysis.")
    st.info("Tip: You can export a CSV directly from Jira's 'Issues' tab.")
    st.stop()  # This prevents the rest of the code from running/crashing
