import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the "Export"
df = pd.read_csv('jira_export.csv')

# 2. Calculation: Velocity (Sum of Story Points for 'Done' tasks)
# In Java 2, this would be a loop with an if-statement and a running total.
velocity = df[df['Status'] == 'Done']['Story Points'].sum()

# 3. Risk Assessment: High/Critical tasks not yet 'Done'
risks = df[(df['Priority'].isin(['High', 'Critical'])) & (df['Status'] != 'Done')]

# 4. Visualization: Status Distribution
status_counts = df['Status'].value_counts()

# --- The "Executive Summary" Output ---
print("="*30)
print("PROJECT HEALTH DASHBOARD")
print("="*30)
print(f"Current Velocity: {velocity} Story Points")
print(f"High Risk Items: {len(risks)}")
if not risks.empty:
    print("\nAttention Needed On:")
    print(risks[['Issue Key', 'Summary', 'Priority']])
print("="*30)

# 5. Create the Chart
status_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['#66b3ff','#99ff99','#ffcc99'])
plt.title('Task Status Distribution')
plt.ylabel('') # Hides the 'Status' label on the side
plt.savefig('status_chart.png')
print("\nDashboard chart saved as 'status_chart.png'")