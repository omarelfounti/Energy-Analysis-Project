def group_data(df, interval):
    if interval == "Daily":
        return df.groupby('Date').agg(
            Consumption=('Energy (kWh)', 'sum'),
            Bill=('Hourly Bill (EUR)', 'sum'),
            Avg_Price=('Price (EUR/kWh)', 'mean'),
            Avg_Temperature=('Temperature', 'mean')
        ).reset_index()
    elif interval == "Weekly":
        return df.groupby('Week').agg(
            Consumption=('Energy (kWh)', 'sum'),
            Bill=('Hourly Bill (EUR)', 'sum'),
            Avg_Price=('Price (EUR/kWh)', 'mean'),
            Avg_Temperature=('Temperature', 'mean')
        ).reset_index()
    else:  
        return df.groupby('Month').agg(
            Consumption=('Energy (kWh)', 'sum'),
            Bill=('Hourly Bill (EUR)', 'sum'),
            Avg_Price=('Price (EUR/kWh)', 'mean'),
            Avg_Temperature=('Temperature', 'mean')
        ).reset_index()
