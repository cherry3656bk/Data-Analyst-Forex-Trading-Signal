import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("="*60)
print("DATA ANALYST FOREX TRADING SIGNAL")
print("="*60)

# Load datasets
forex = pd.read_csv("Forex_price_data.csv")
mc = pd.read_csv("Mc_scenarios.csv")
trade = pd.read_csv("Trade_log.csv")

print("\nForex Data")
print(forex.head())

print("\nMonte Carlo Scenarios")
print(mc.head())

print("\nTrade Log")
print(trade.head())

print("\nMissing Values")
print(forex.isnull().sum())
print(mc.isnull().sum())
print(trade.isnull().sum())

print("\nSummary Statistics")
print(forex.describe())

# Plot first numeric forex column
forex_num = forex.select_dtypes(include=np.number).columns

if len(forex_num) > 0:
    plt.figure(figsize=(8,5))
    plt.plot(forex[forex_num[0]])
    plt.title("Forex Price Trend")
    plt.xlabel("Observation")
    plt.ylabel(forex_num[0])
    plt.tight_layout()
    plt.savefig("forex_price_trend.png")
    plt.close()

# Plot first numeric Monte Carlo column
mc_num = mc.select_dtypes(include=np.number).columns

if len(mc_num) > 0:
    plt.figure(figsize=(8,5))
    plt.hist(mc[mc_num[0]], bins=30)
    plt.title("Monte Carlo Distribution")
    plt.tight_layout()
    plt.savefig("mc_distribution.png")
    plt.close()

print("\nAnalysis completed successfully.")