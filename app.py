import streamlit as st
import pandas as pd

# Page title
st.set_page_config(page_title="HR Analytics Dashboard", layout="wide")
st.title("HR Analytics Dashboard")

# Load HR data
df = pd.read_csv("hr_data.csv")

# Sidebar filter
st.sidebar.header("Filter Options")
department = st.sidebar.multiselect(
    "Select Department",
    options=df["Department"].unique(),
    default=df["Department"].unique()
)

filtered_df = df[df["Department"].isin(department)]

# KPI section
col1, col2, col3 = st.columns(3)
col1.metric("Average Satisfaction", round(filtered_df["Satisfaction"].mean(), 2))
col2.metric("Average Salary", f"${int(filtered_df['Salary'].mean()):,}")
col3.metric("Number of Employees", filtered_df.shape[0])

st.divider()

# Chart: Average Satisfaction by Department using Streamlit built-in chart
st.subheader("Average Satisfaction by Department")
avg_satisfaction = filtered_df.groupby("Department")["Satisfaction"].mean().reset_index()
st.bar_chart(data=avg_satisfaction, x="Department", y="Satisfaction")

st.divider()

# Show filtered data table
st.subheader("Employee Data")
st.dataframe(filtered_df)

# Download filtered data as CSV
csv = filtered_df.to_csv(index=False)
st.download_button(
    label="📥 Download Filtered Data (CSV)",
    data=csv,
    file_name="filtered_hr_data.csv",
    mime="text/csv"
)
