import streamlit as st
import pandas as pd
import altair as alt

data = {'total_patients': [42820]}
df = pd.DataFrame(data).reset_index()

# Create a bar chart using Altair
chart = alt.Chart(df).mark_bar().encode(
    x='index',
    y='total_patients'
)

# Set the chart title and axis labels
chart = chart.properties(
    title={
        "text": "Total Patients",
        "subtitle": "Number of patients in the dataset"
    },
    x=alt.X(title="Total Patients"),
    y=alt.Y(title=None)
)

# Display the chart using Streamlit
st.altair_chart(chart, use_container_width=True)