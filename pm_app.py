import streamlit as st

# --- UI Header ---
st.title("🚀 PM Priority Dashboard")
st.write("Enter project metrics to calculate the priority score.")

# --- Layout: Side-by-side columns ---
col1, col2 = st.columns(2)

with col1:
    project_name = st.text_input("Project Name", value="New Feature")
    impact = st.slider("Business Impact (1-10)", 1, 10, 5)

with col2:
    effort = st.slider("Development Effort (1-10)", 1, 10, 5)
    risk = st.selectbox("Risk Level", ["Low", "Medium", "High"])

# --- Logic: Simple Weighted Calculation ---
# Risk multiplier
risk_map = {"Low": 1.0, "Medium": 1.5, "High": 2.0}
score = (impact * 10) / (effort * risk_map[risk])

# --- UI Output ---
st.divider()
st.subheader(f"Analysis for: {project_name}")

# Using a "Metric" component (very common in modern dashboards)
st.metric(label="Priority Score", value=f"{score:.2f}")

if score > 5:
    st.success("Verdict: High Priority - Move to Sprint")
else:
    st.warning("Verdict: Backlog - Low ROI")

# ROI Formula in LaTeX
st.latex(r"Score = \frac{Impact \times 10}{Effort \times Risk}")

# --- New AI Feature ---
st.header("🤖 AI Risk Consultant")
project_description = st.text_area(
    "Describe the project context:",
    placeholder="e.g. This project involves migrating a legacy Java 2 database to a cloud-native environment...",
)

if st.button("Generate Expert Analysis"):
    if project_description:
        with st.spinner("Consulting AI..."):
            # In a real app, you'd call an API here.
            # For now, let's simulate the AI's logic.
            ai_insight = (
                f"Based on an impact of {impact} and {risk} risk, "
                f"the primary concern for '{project_name}' is technical debt. "
                "Recommendation: Conduct a code audit before the first sprint."
            )
            st.info(ai_insight)
    else:
        st.error("Please enter a description first!")
