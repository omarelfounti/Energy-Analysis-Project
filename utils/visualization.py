import matplotlib.pyplot as plt

def plot_metrics(grouped_df, interval):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle(f'{interval} Energy Metrics')

    axes[0, 0].plot(grouped_df.iloc[:, 0], grouped_df['Consumption'], label='Consumption')
    axes[0, 0].set_title(f'{interval} Consumption')
    axes[0, 0].set_xlabel(interval)
    axes[0, 0].set_ylabel('kWh')

    axes[0, 1].plot(grouped_df.iloc[:, 0], grouped_df['Bill'], label='Bill', color='orange')
    axes[0, 1].set_title(f'{interval} Bill')
    axes[0, 1].set_xlabel(interval)
    axes[0, 1].set_ylabel('EUR')

    axes[1, 0].plot(grouped_df.iloc[:, 0], grouped_df['Avg_Price'], label='Average Price', color='green')
    axes[1, 0].set_title(f'{interval} Average Price')
    axes[1, 0].set_xlabel(interval)
    axes[1, 0].set_ylabel('EUR/kWh')

    axes[1, 1].plot(grouped_df.iloc[:, 0], grouped_df['Avg_Temperature'], label='Average Temperature', color='red')
    axes[1, 1].set_title(f'{interval} Average Temperature')
    axes[1, 1].set_xlabel(interval)
    axes[1, 1].set_ylabel('°C')

    plt.tight_layout(rect=[0, 0, 1, 0.96]) 
    return fig
