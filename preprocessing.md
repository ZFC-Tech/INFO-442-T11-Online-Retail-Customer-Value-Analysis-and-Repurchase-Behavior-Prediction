# Data Preprocessing Log

## Dataset Information
- Original file: online_retail(1).csv
- Original rows: 541,909
- After removing duplicates: 536,641
- After dropping missing values: 401,604
- After removing outliers: 397,594
- **Final rows**: 388,804

---

## Data Quality Overview

![Sales vs Returns](fig4_sales_vs_returns.png)
*Figure 1: Transaction type distribution – Returns account for 0.0% of total transactions*

---

## Preprocessing Steps and Justifications

### 1. Remove duplicate rows
- **Operation**: `df.drop_duplicates()`
- **Rows removed**: 5,268
- **Reason**: Ensure each transaction is unique to avoid double counting.

### 2. Handle missing values
- **Columns**: `CustomerID`, `Description`
- **Missing before removal**: CustomerID: 135,037 (24.92%), Description: 1,454 (0.27%)
- **Operation**: Drop rows where either column is null
- **Rows removed**: 135,037
- **Reason**: Missing CustomerID prevents customer-level analysis; missing Description makes product identification impossible.

### 3. Data type conversion
- `CustomerID`: `float` → `int`
- `InvoiceDate`: `object` → `datetime`
- `InvoiceNo`: `object` → `str`
- **Reason**: Enables time series analysis and proper handling of invoice prefixes.

### 4. Mark return transactions
- **Operation**: Check if `InvoiceNo` starts with 'C'
- **New column**: `TransactionType` (Sale / Return)
- **Reason**: Returns need to be analyzed separately from normal sales. Both are retained in the dataset.

### 5. Outlier treatment
- **Column**: `Quantity` (absolute values)
- **Method**: Keep data within 1st ~ 99th percentiles
- **Rows removed**: 4,010
- **Reason**: Extremely large quantities are likely data entry errors.

### 6. Feature engineering
- `TotalAmount` = `Quantity` × `UnitPrice`
- Time features: `Year`, `Month`, `Day`, `Hour`, `Weekday`
- **Reason**: Enables revenue calculation and temporal pattern analysis.

### 7. Standardize country names
- **Operation**: Strip whitespace and convert to title case
- **Reason**: Ensures consistency when grouping by country.

---

## Output Files
- Cleaned data: `online_retail_cleaned.csv`
- This log: `preprocessing.md`
- Data quality summary: `summary.md`
- Visualization images: `fig1.png` to `fig8.png`
