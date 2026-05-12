```python
# =========================================
# Online Retail Dataset Analysis
# Research-Level EDA + Statistical Analysis
# =========================================

# ---------- 1. Import Libraries ----------
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency


# ---------- 2. Load Dataset ----------
df = pd.read_csv("online_retail.csv", encoding='ISO-8859-1')


# ---------- 3. Basic Info ----------
print("="*60)
print("DATASET SHAPE")
print(df.shape)

print("\nFIRST 5 ROWS")
print(df.head())

print("\nDATA INFO")
print(df.info())

print("\nMISSING VALUES")
print(df.isnull().sum())

```

    ============================================================
    DATASET SHAPE
    (541909, 8)
    
    FIRST 5 ROWS
      InvoiceNo StockCode                          Description  Quantity  \
    0    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6   
    1    536365     71053                  WHITE METAL LANTERN         6   
    2    536365    84406B       CREAM CUPID HEARTS COAT HANGER         8   
    3    536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6   
    4    536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6   
    
               InvoiceDate  UnitPrice  CustomerID         Country  
    0  2010-12-01 08:26:00       2.55     17850.0  United Kingdom  
    1  2010-12-01 08:26:00       3.39     17850.0  United Kingdom  
    2  2010-12-01 08:26:00       2.75     17850.0  United Kingdom  
    3  2010-12-01 08:26:00       3.39     17850.0  United Kingdom  
    4  2010-12-01 08:26:00       3.39     17850.0  United Kingdom  
    
    DATA INFO
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 541909 entries, 0 to 541908
    Data columns (total 8 columns):
     #   Column       Non-Null Count   Dtype  
    ---  ------       --------------   -----  
     0   InvoiceNo    541909 non-null  object 
     1   StockCode    541909 non-null  object 
     2   Description  540455 non-null  object 
     3   Quantity     541909 non-null  int64  
     4   InvoiceDate  541909 non-null  object 
     5   UnitPrice    541909 non-null  float64
     6   CustomerID   406829 non-null  float64
     7   Country      541909 non-null  object 
    dtypes: float64(2), int64(1), object(5)
    memory usage: 33.1+ MB
    None
    
    MISSING VALUES
    InvoiceNo           0
    StockCode           0
    Description      1454
    Quantity            0
    InvoiceDate         0
    UnitPrice           0
    CustomerID     135080
    Country             0
    dtype: int64
    


```python

# =========================================
# DATA CLEANING
# =========================================

# ---------- 4. Remove Missing CustomerID ----------
df = df.dropna(subset=['CustomerID'])

# ---------- 5. Convert Date ----------
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# ---------- 6. Remove Cancellations ----------
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]

# ---------- 7. Remove Negative Quantity ----------
df = df[df['Quantity'] > 0]

# ---------- 8. Remove Negative Price ----------
df = df[df['UnitPrice'] > 0]

# ---------- 9. Create Total Price ----------
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

print("\nCLEANED DATA SHAPE")
print(df.shape)

```

    
    CLEANED DATA SHAPE
    (397884, 9)
    


```python

# =========================================
# CREATE REPEAT CUSTOMER LABEL
# =========================================

# Count invoices per customer
invoice_count = df.groupby('CustomerID')['InvoiceNo'].nunique()

# Repeat customer = more than 1 invoice
repeat_customer = (invoice_count > 1).astype(int)

repeat_df = repeat_customer.reset_index()
repeat_df.columns = ['CustomerID', 'RepeatCustomer']

df = df.merge(repeat_df, on='CustomerID')

print("\nREPEAT CUSTOMER DISTRIBUTION")
print(
    df[['CustomerID', 'RepeatCustomer']]
    .drop_duplicates()['RepeatCustomer']
    .value_counts(normalize=True)
)

```

    
    REPEAT CUSTOMER DISTRIBUTION
    RepeatCustomer
    1    0.655832
    0    0.344168
    Name: proportion, dtype: float64
    


```python

# =========================================
# EDA SECTION
# =========================================

# ---------- 10. Sales Distribution ----------
# Research-level visualization using log transform

plt.figure(figsize=(10,6))

sales_filtered = df[
    df['TotalPrice'] < df['TotalPrice'].quantile(0.99)
]

plt.hist(
    np.log1p(sales_filtered['TotalPrice']),
    bins=50
)

plt.title("Log-Transformed Sales Distribution")
plt.xlabel("Log(Total Price)")
plt.ylabel("Frequency")

plt.show()

# ---------- 11. Top Countries ----------
# Excluding UK because it dominates the dataset

country_counts = df[
    df['Country'] != 'United Kingdom'
]['Country'].value_counts().head(10)

plt.figure(figsize=(10,6))

country_counts.plot(kind='bar')

plt.title("Top Countries Excluding UK")
plt.xlabel("Country")
plt.ylabel("Transactions")

plt.xticks(rotation=45)

plt.show()

# ---------- 12. Monthly Sales Trend ----------

df['Month'] = df['InvoiceDate'].dt.to_period('M')

monthly_sales = df.groupby('Month')['TotalPrice'].sum()

plt.figure(figsize=(12,5))

monthly_sales.plot()

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid(True)

plt.show()

# ---------- 13. Top Products ----------

top_products = (
    df.groupby('Description')['Quantity']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,6))

top_products.plot(kind='bar')

plt.title("Top 10 Products")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")

plt.xticks(rotation=75)

plt.show()

```


    
![png](retail_analysis_files/retail_analysis_3_0.png)
    



    
![png](retail_analysis_files/retail_analysis_3_1.png)
    



    
![png](retail_analysis_files/retail_analysis_3_2.png)
    



    
![png](retail_analysis_files/retail_analysis_3_3.png)
    



```python

# =========================================
# CUSTOMER ANALYSIS
# =========================================

# ---------- 14. Customer Purchase Frequency ----------

customer_freq = df.groupby('CustomerID')['InvoiceNo'].nunique()

freq_filtered = customer_freq[
    customer_freq < customer_freq.quantile(0.99)
]

plt.figure(figsize=(10,6))

plt.hist(freq_filtered, bins=40)

plt.title("Customer Purchase Frequency (99% filtered)")
plt.xlabel("Number of Purchases")
plt.ylabel("Customers")

plt.show()

# ---------- 15. Log Purchase Frequency ----------

plt.figure(figsize=(10,6))

plt.hist(np.log1p(customer_freq), bins=40)

plt.title("Log Purchase Frequency Distribution")
plt.xlabel("Log(Number of Purchases)")
plt.ylabel("Customers")

plt.show()

# ---------- 16. Top Customers ----------

top_customers = (
    df.groupby('CustomerID')['TotalPrice']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTOP 10 CUSTOMERS BY REVENUE")
print(top_customers)

```


    
![png](retail_analysis_files/retail_analysis_4_0.png)
    



    
![png](retail_analysis_files/retail_analysis_4_1.png)
    


    
    TOP 10 CUSTOMERS BY REVENUE
    CustomerID
    14646.0    280206.02
    18102.0    259657.30
    17450.0    194550.79
    16446.0    168472.50
    14911.0    143825.06
    12415.0    124914.53
    14156.0    117379.63
    17511.0     91062.38
    16029.0     81024.84
    12346.0     77183.60
    Name: TotalPrice, dtype: float64
    


```python

# =========================================
# RFM ANALYSIS
# =========================================

# ---------- 17. Snapshot Date ----------

snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)

# ---------- 18. Calculate RFM ----------

rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
    'InvoiceNo': 'nunique',
    'TotalPrice': 'sum'
})

rfm.columns = ['Recency', 'Frequency', 'Monetary']

print("\nRFM SUMMARY")
print(rfm.head())

print("\nRFM STATISTICS")
print(rfm.describe())

# ---------- 19. RFM Scatter Plot ----------

plt.figure(figsize=(10,6))

plt.scatter(
    np.log1p(rfm['Frequency']),
    np.log1p(rfm['Monetary']),
    alpha=0.5
)

plt.title("Log Frequency vs Log Monetary")
plt.xlabel("Log(Frequency)")
plt.ylabel("Log(Monetary)")

plt.show()

```

    
    RFM SUMMARY
                Recency  Frequency  Monetary
    CustomerID                              
    12346.0         326          1  77183.60
    12347.0           2          7   4310.00
    12348.0          75          4   1797.24
    12349.0          19          1   1757.55
    12350.0         310          1    334.40
    
    RFM STATISTICS
               Recency    Frequency       Monetary
    count  4338.000000  4338.000000    4338.000000
    mean     92.536422     4.272015    2054.266460
    std     100.014169     7.697998    8989.230441
    min       1.000000     1.000000       3.750000
    25%      18.000000     1.000000     307.415000
    50%      51.000000     2.000000     674.485000
    75%     142.000000     5.000000    1661.740000
    max     374.000000   209.000000  280206.020000
    


    
![png](retail_analysis_files/retail_analysis_5_1.png)
    



```python

# =========================================
# PARETO ANALYSIS
# =========================================

# ---------- 20. Pareto Revenue Analysis ----------

customer_revenue = (
    df.groupby('CustomerID')['TotalPrice']
    .sum()
    .sort_values(ascending=False)
)

cumulative = customer_revenue.cumsum() / customer_revenue.sum()

plt.figure(figsize=(10,6))

plt.plot(range(len(cumulative)), cumulative)

plt.axhline(
    y=0.8,
    linestyle='--'
)

plt.title("Pareto Analysis of Customer Revenue")
plt.xlabel("Customers")
plt.ylabel("Cumulative Revenue Share")

plt.grid(True)

plt.show()

```


    
![png](retail_analysis_files/retail_analysis_6_0.png)
    



```python

# =========================================
# BOXPLOT ANALYSIS
# =========================================

# ---------- 21. Boxplot for Outlier Detection ----------

plt.figure(figsize=(10,6))

plt.boxplot(
    sales_filtered['TotalPrice'],
    vert=False
)

plt.title("Boxplot of Total Price")

plt.xlabel("Total Price")

plt.show()

```


    
![png](retail_analysis_files/retail_analysis_7_0.png)
    



```python

# =========================================
# STATISTICAL ANALYSIS
# =========================================

print("\n" + "="*60)
print("STATISTICAL ANALYSIS")
print("="*60)

# ---------- 22. Spending Difference ----------

customer_spending = df.groupby('CustomerID').agg({
    'TotalPrice': 'sum',
    'RepeatCustomer': 'first'
})

repeat_spending = customer_spending[
    customer_spending['RepeatCustomer'] == 1
]['TotalPrice']

nonrepeat_spending = customer_spending[
    customer_spending['RepeatCustomer'] == 0
]['TotalPrice']

t_stat, p_value = ttest_ind(
    repeat_spending,
    nonrepeat_spending,
    equal_var=False
)

print("\nT-TEST: Spending Difference")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

if p_value < 0.05:
    print("Result: Significant spending difference exists.")
else:
    print("Result: No significant difference.")

# ---------- 23. Country Repeat Rate ----------

country_repeat = (
    df.groupby('Country')['RepeatCustomer']
    .mean()
)

top_country_repeat = (
    country_repeat
    .sort_values(ascending=False)
    .head(10)
)

print("\nTOP COUNTRIES BY REPEAT RATE")
print(top_country_repeat)

```

    
    ============================================================
    STATISTICAL ANALYSIS
    ============================================================
    
    T-TEST: Spending Difference
    T-statistic: 11.8562
    P-value: 0.0000
    Result: Significant spending difference exists.
    
    TOP COUNTRIES BY REPEAT RATE
    Country
    Australia             1.000000
    Iceland               1.000000
    European Community    1.000000
    EIRE                  1.000000
    Czech Republic        1.000000
    Singapore             1.000000
    Unspecified           1.000000
    Lithuania             1.000000
    Netherlands           0.977957
    Channel Islands       0.958556
    Name: RepeatCustomer, dtype: float64
    


```python

# =========================================
# BUSINESS INSIGHTS
# =========================================

print("\n" + "="*60)
print("BUSINESS INSIGHTS")
print("="*60)

# ---------- 24. Average Spending ----------

print("\n1. Average Customer Spending")

print(
    customer_spending
    .groupby('RepeatCustomer')['TotalPrice']
    .mean()
)

# ---------- 25. Purchase Frequency ----------

print("\n2. Purchase Frequency Statistics")

print(customer_freq.describe())

# ---------- 26. Best Selling Product ----------

print("\n3. Best Selling Product")

print(top_products.head(1))

# ---------- 27. Highest Revenue Countries ----------

print("\n4. Highest Revenue Countries")

print(
    df.groupby('Country')['TotalPrice']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

# ---------- 28. RFM Insights ----------

print("\n5. RFM Insights")

print(
    rfm[['Recency', 'Frequency', 'Monetary']]
    .describe()
)

print("\nAnalysis Completed Successfully.")
```

    
    ============================================================
    BUSINESS INSIGHTS
    ============================================================
    
    1. Average Customer Spending
    RepeatCustomer
    0     412.800891
    1    2915.675280
    Name: TotalPrice, dtype: float64
    
    2. Purchase Frequency Statistics
    count    4338.000000
    mean        4.272015
    std         7.697998
    min         1.000000
    25%         1.000000
    50%         2.000000
    75%         5.000000
    max       209.000000
    Name: InvoiceNo, dtype: float64
    
    3. Best Selling Product
    Description
    PAPER CRAFT , LITTLE BIRDIE    80995
    Name: Quantity, dtype: int64
    
    4. Highest Revenue Countries
    Country
    United Kingdom    7308391.554
    Netherlands        285446.340
    EIRE               265545.900
    Germany            228867.140
    France             209024.050
    Name: TotalPrice, dtype: float64
    
    5. RFM Insights
               Recency    Frequency       Monetary
    count  4338.000000  4338.000000    4338.000000
    mean     92.536422     4.272015    2054.266460
    std     100.014169     7.697998    8989.230441
    min       1.000000     1.000000       3.750000
    25%      18.000000     1.000000     307.415000
    50%      51.000000     2.000000     674.485000
    75%     142.000000     5.000000    1661.740000
    max     374.000000   209.000000  280206.020000
    
    Analysis Completed Successfully.
    
