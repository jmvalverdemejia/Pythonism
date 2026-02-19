import pandas as pd
import matplotlib.pyplot as plt

# --- STEP 1: The Data (The "Merger") ---
# Imagine these came from two different Excel files
projects = pd.DataFrame({
    "Project": ["Alpha", "Beta", "Gamma"],
    "Status": ["Active", "Active", "On Hold"]
})

budgets = pd.DataFrame({
    "Project": ["Alpha", "Beta", "Gamma"],
    "Spend": [5000, 8500, 2000]
})

# In Java 2, merging would be a double 'for' loop or a complex HashMap.
# In Python/Pandas, it's one line (an Inner Join):
merged_data = pd.merge(projects, budgets, on="Project")

# --- STEP 2: The Visualizer ---
# Let's create a bar chart of the spend per project
print("Generating dashboard...")

plt.bar(merged_data["Project"], merged_data["Spend"], color='skyblue')
plt.title('Project Budget Overview 2026')
plt.xlabel('Project Name')
plt.ylabel('Spend ($)')

# Save the chart as an image
plt.savefig('project_spend_chart.png')
print("Done! Check your folder for 'project_spend_chart.png'")