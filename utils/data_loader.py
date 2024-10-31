import pandas as pd

def load_data(file1_path, file2_path):
    file1_df = pd.read_csv(file1_path)
    file2_df = pd.read_csv(file2_path, delimiter=';')
    
    file1_df['Time'] = pd.to_datetime(file1_df['Time'], format='%d-%m-%Y %H:%M:%S')
    file2_df['Time'] = pd.to_datetime(file2_df['Time'].str.strip(), format='%d.%m.%Y %H:%M')
    merged_df = pd.merge(file1_df, file2_df, on='Time', how='inner')
    
    merged_df['Price (EUR/kWh)'] = merged_df['Price (cent/kWh)'] / 100
    merged_df['Energy (kWh)'] = merged_df['Energy (kWh)'].str.replace(',', '').astype(float)
    merged_df['Temperature'] = merged_df['Temperature'].str.replace(',', '.').astype(float)
    merged_df['Hourly Bill (EUR)'] = merged_df['Price (EUR/kWh)'] * merged_df['Energy (kWh)']
    
    merged_df['Date'] = merged_df['Time'].dt.date
    merged_df['Week'] = merged_df['Time'].dt.isocalendar().week
    merged_df['Month'] = merged_df['Time'].dt.to_period('M')
    
    return merged_df
