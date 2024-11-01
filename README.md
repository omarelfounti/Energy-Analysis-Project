Energy Analysis Project

This project is an interactive data analysis application built using Streamlit to analyze energy consumption and pricing data. It helps users visualize and understand their energy usage over time, including trends in consumption, cost, average energy price, and temperature. Users can select date ranges and grouping intervals to explore their data in daily, weekly, or monthly summaries.

Data Sources
Price Data: Sourced from Porssisahko.
From personal energy account data via energiatili.fi (login required).
Key Features
Allows users to choose specific time intervals for analysis.
View data summaries by day, week, or month.
Line graphs show trends in consumption, cost, average price, and temperature.


Installation
Clone the repository:
git clone https://github.com/omarelfounti/Energy-Analysis-Project.git

Navigate to the project: https://omarelfounti-energy-analysis-project-app-x7vcx2.streamlit.app/

Make sure you have Python and pip installed. Then, install the necessary packages:


pip install -r requirements.txt
Note: The requirements.txt should include streamlit, pandas, and matplotlib.

Place Data Files: Add the necessary data files to the data folder as described in the project structure.


Run the Streamlit app with the following command:
streamlit run app.py
This will start a local server, and you can access the app in your web browser at http://localhost:8501.


Choose the date range you want to analyze.
Choose between daily, weekly, or monthly grouping.
The app displays line charts for energy consumption, cost, average price, and temperature based on your selections.

This project is licensed under the MIT License.
