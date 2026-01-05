import pandas as pd
import numpy as np
from datetime import datetime, timedelta


data = {
    'Month': pd.date_range(start='2024-01-01', periods=12, freq='M'),
    'Revenue': [12000, 15000, 14000, 18000, 22000, 25000, 24000, 30000, 32000, 35000, 38000, 42000],
    'OpEx_Salaries': [8000, 8000, 9000, 9500, 10000, 10000, 12000, 12500, 13000, 14000, 14500, 15000],
    'OpEx_Server_Infra': [500, 520, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]
}

df = pd.DataFrame(data)

def calculate_burn_metrics(dataframe):
    """
    Calculates operational burn rate and net profit margin.
    """
    dataframe['Total_OpEx'] = dataframe['OpEx_Salaries'] + dataframe['OpEx_Server_Infra']
    dataframe['Net_Profit'] = dataframe['Revenue'] - dataframe['Total_OpEx']
    dataframe['Margin_%'] = round((dataframe['Net_Profit'] / dataframe['Revenue']) * 100, 2)
    
    return dataframe

def forecast_next_quarter(dataframe):
    """
    Simple linear projection for the next 3 months based on rolling average.
    """
    last_3_avg_growth = dataframe['Revenue'].pct_change().tail(3).mean()
    last_revenue = dataframe['Revenue'].iloc[-1]
    
    projection = []
    current_date = dataframe['Month'].iloc[-1]
    
    print(f"--- Q1 2025 PROJECTION (Growth Factor: {round(last_3_avg_growth*100, 2)}%) ---")
    
    for i in range(1, 4):
        next_rev = last_revenue * (1 + last_3_avg_growth)
        current_date += timedelta(days=30)
        print(f"Month {i}: Predicted Revenue ${round(next_rev, 2)}")
        last_revenue = next_rev

# Execution
processed_df = calculate_burn_metrics(df)
print(processed_df.tail(6))
print("\n")
forecast_next_quarter(processed_df)
