import streamlit as st
import pandas as pd
from utils.data_loader import load_data
from utils.data_processing import group_data
from utils.visualizations import plot_metrics


file1_path = 'data/sahkon-hinta-010121-240924.csv'
file2_path = 'data/Electricity_20-09-2024.csv'
merged_df = load_data(file1_path, file2_path)


st.sidebar.header("Select Analysis Parameters")
start_date = st.sidebar.date_input("Select Start Date", value=pd.to_datetime("2021-01-01"))
end_date = st.sidebar.date_input("Select End Date", value=pd.to_datetime("2024-09-24"))
interval = st.sidebar.selectbox("Select Grouping Interval", ("Daily", "Weekly", "Monthly"))


filtered_df = merged_df[(merged_df['Date'] >= pd.to_datetime(start_date).date()) &
                        (merged_df['Date'] <= pd.to_datetime(end_date).date())]


grouped_df = group_data(filtered_df, interval)

if interval == "Monthly":
    grouped_df['Month'] = grouped_df['Month'].dt.to_timestamp()


st.header(f"{interval} Summary from {start_date} to {end_date}")
st.write(grouped_df)


fig = plot_metrics(grouped_df, interval)
st.pyplot(fig)
