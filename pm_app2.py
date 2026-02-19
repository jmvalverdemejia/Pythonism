import streamlit as st
import pandas as pd

st.title("📊 Live Jira Dashboard")

# 1. Load the Data
# In Java 2, this was 50 lines of IO code. In Python, it's one.
try:
    df = pd.read_csv("jira_export.csv")
except FileNotFoundError:
    st.error("CSV file not found! Please make sure 'jira_export.csv' is in the folder.")
    st.stop()

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
