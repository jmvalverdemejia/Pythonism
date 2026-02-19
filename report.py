import pandas as pd

# 1. Create a Dictionary (Like a HashMap, but easier to write)
project_data = {
    "Task Name": ["Database Migration", "API Integration", "User Acceptance Testing"],
    "Owner": ["Alice", "Bob", "Charlie"],
    "Status": ["Completed", "In Progress", "Not Started"],
    "Progress (%)": [100, 65, 0]
}

# 2. Convert to a DataFrame (Think of this as an in-memory SQL Table or a Spreadsheet)
df = pd.DataFrame(project_data)

# 3. Perform a "Management Calculation"
# Let's say we want to see only tasks that are behind (less than 100% progress)
pending_tasks = df[df["Progress (%)"] < 100]

# 4. Save to Excel
# No FileOutputStreams or manual closing of files needed!
pending_tasks.to_excel("Pending_Tasks_Report.xlsx", index=False)

print("Report generated successfully! Check your folder for the Excel file.")