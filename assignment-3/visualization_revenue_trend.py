# CSCE 5300 - Assignment 3
# Part B: 1D Visualization - line plot of a time series
#
# Original scenario: plot the cleaned monthly revenue trend for the same
# mobile hair-styling business used in Part A (Cleansing 4), so the
# preprocessing step and the analysis step tell one connected story.
# The variable names and data values are original; only the general
# "line plot of a time series with plt.plot()" idea follows the
# course's population-growth example.

import matplotlib
matplotlib.use('Agg')  # render to file without a display
import matplotlib.pyplot as plt
import pandas as pd

# Load the cleaned (forward-filled) revenue series produced by Part A.
cleaned_revenue = pd.read_csv(
    'cleaned_monthly_revenue.csv', index_col=0
)['monthly_revenue_usd']

operating_months = cleaned_revenue.index.tolist()
revenue_totals_usd = cleaned_revenue.values

plt.figure(figsize=(8, 5))
plt.plot(operating_months, revenue_totals_usd, marker='o',
         color='#1E5631', linewidth=2)
plt.title("Mobile Hair-Styling Business: Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (USD)")
plt.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig('monthly_revenue_trend.png', dpi=150)
print("Saved line plot to monthly_revenue_trend.png")

print("\nData plotted (cleaned monthly revenue):")
print(cleaned_revenue)
