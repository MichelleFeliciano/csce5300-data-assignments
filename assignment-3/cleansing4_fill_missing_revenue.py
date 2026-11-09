# CSCE 5300 - Assignment 3
# Part A: Cleansing 4 - Fill NA Forward and Backward
#
# Original scenario (not from the course template): a mobile hair-styling
# business records its total revenue at the end of every month. A few
# months were never logged (the stylist was on the road and forgot to
# enter the total), so those months come into Python as missing values
# (NaN). This script demonstrates two ways to fill those gaps: carrying
# the last known month's total forward, and borrowing the next known
# month's total backward.
#
# All variable names, the business scenario, and the data values below
# are original and unrelated to the course's reindex()/df/one-two-three
# template example.

import pandas as pd
import numpy as np

# Twelve calendar months of one operating year.
service_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Recorded monthly revenue in US dollars. np.nan marks a month whose
# total was never logged.
monthly_revenue_usd = pd.Series(
    [2150.0, np.nan, 2480.0, 2600.0, np.nan, np.nan,
     3100.0, 2950.0, np.nan, 3300.0, 3450.0, 3600.0],
    index=service_months,
    name='monthly_revenue_usd'
)

print("Step 1 - Raw monthly revenue, with unrecorded months as NaN:")
print(monthly_revenue_usd)

# How many months are missing, and which ones.
missing_month_flags = monthly_revenue_usd.isnull()
print("\nStep 2 - Which months are missing?")
print(missing_month_flags)
print(f"\nTotal unrecorded months: {int(missing_month_flags.sum())}")

# Forward-fill: an unrecorded month is assumed to match the most recent
# month that WAS recorded (reasonable if revenue is fairly steady
# month-to-month and the business simply forgot to log a number).
revenue_filled_forward = monthly_revenue_usd.ffill()
print("\nStep 3 - Forward-filled revenue (missing month repeats the prior "
      "recorded month's total):")
print(revenue_filled_forward)

# Backward-fill: an unrecorded month instead borrows the next recorded
# month's total. Shown for comparison against the forward-fill result.
revenue_filled_backward = monthly_revenue_usd.bfill()
print("\nStep 4 - Backward-filled revenue (missing month borrows the next "
      "recorded month's total):")
print(revenue_filled_backward)

# Save the forward-filled series to a small CSV so Part B (the 1D line
# plot) can plot the cleaned trend without recomputing it.
revenue_filled_forward.to_csv('cleaned_monthly_revenue.csv', header=True)
print("\nSaved cleaned (forward-filled) series to cleaned_monthly_revenue.csv")
