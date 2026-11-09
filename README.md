# CSCE 5300 Assignments

Coursework from CSCE 5300 (Introduction to Big Data and Data Science), University of North Texas, Fall 2026. Both assignments use an original scenario about a mobile hair-styling business.

## assignment-2: SQL SELECT statements
- `select_statement_code.sql` creates a `SalonBookings` table with 10 sample rows and three queries: a basic column SELECT, a filter with sorting (`WHERE` plus `ORDER BY`), and a text-based filter.
- `Assignment2_Report.pdf` explains the problem, method and code.

## assignment-3: Data cleansing and visualization
- `cleansing4_fill_missing_revenue.py` fills missing monthly revenue values with pandas forward-fill and backward-fill and saves the forward-filled series to a CSV.
- `visualization_revenue_trend.py` plots that cleaned series as a line chart and saves `monthly_revenue_trend.png`. Run the cleansing script first, since the plot reads its output file.
- `Assignment3_Feliciano.pdf` is the report.

Requires Python with `pandas`, `numpy` and `matplotlib`.
