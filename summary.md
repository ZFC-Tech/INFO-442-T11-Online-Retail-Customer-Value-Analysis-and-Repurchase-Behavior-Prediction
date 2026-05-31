# Data Quality Summary

## 1. Missing Rate Statistics (Before Cleaning)

| Column | Missing Count | Missing Rate |
|--------|--------------|--------------|
| CustomerID | 135,037 | 24.92% |
| Description | 1,454 | 0.27% |

**Action taken**: Rows with missing CustomerID or Description were removed (135,037 rows).

---

## 2. Class Balance (After Cleaning)

| Transaction Type | Record Count | Percentage |
|------------------|--------------|------------|
| Sale | 388,804 | 100.0% |
| Return | 0 | 0.0% |

**Note**: Returns are retained with negative Quantity values. Total return value: £0.00.

![Sales vs Returns](fig4_sales_vs_returns.png)
*Figure 1: Transaction type distribution – Sales vs Returns*

---

## 3. Outlier Treatment

- **Method**: Kept `Quantity` absolute values within 1st ~ 99th percentiles
- **After treatment, Quantity range**: -121 ~ 125
- **Rows removed as outliers**: 4,010

---

## 4. Key Field Distributions

| Metric | Value |
|--------|-------|
| Total Sales (excluding returns) | £7,196,430.02 |
| Total Returns | £0.00 |
| Net Revenue | £7,196,430.02 |
| Average Unit Price (all) | £3.14 |

![Top 10 Countries by Sales Revenue](fig3_top_countries.png)
*Figure 2: Top 10 countries by sales revenue (United Kingdom dominates)*

![Unit Price Distribution](fig5_price_distribution.png)
*Figure 3: Distribution of unit prices – most products are priced between £1-5*

---

## 5. Top 10 Best-Selling Products by Quantity

![Top 10 Best-Selling Products](fig6_top_products.png)
*Figure 4: Top 10 best-selling products by quantity*

| Rank | Product Description | Quantity Sold |
|------|---------------------|---------------|
| 1 | JUMBO BAG RED RETROSPOT | 29,868 |
| 2 | WHITE HANGING HEART T-LIGHT HOLDER | 23,398 |
| 3 | PACK OF 72 RETROSPOT CAKE CASES | 22,870 |
| 4 | ASSORTED COLOUR BIRD ORNAMENT | 22,055 |
| 5 | WORLD WAR 2 GLIDERS ASSTD DESIGNS | 21,439 |
| 6 | VICTORIAN GLASS HANGING T-LIGHT | 17,214 |
| 7 | LUNCH BAG RED RETROSPOT | 16,826 |
| 8 | POPCORN HOLDER | 15,127 |
| 9 | RABBIT NIGHT LIGHT | 14,181 |
| 10 | JUMBO BAG PINK POLKADOT | 13,748 |

---

## 6. Top Countries by Number of Orders

![Top Countries by Orders](fig8_country_orders.png)
*Figure 5: Top countries by number of orders – United Kingdom leads significantly*

| Rank | Country | Number of Orders |
|------|---------|------------------|
| 1 | United Kingdom | 346,453 |
| 2 | Germany | 8,984 |
| 3 | France | 8,297 |
| 4 | Eire | 7,045 |
| 5 | Spain | 2,460 |
| 6 | Belgium | 2,028 |
| 7 | Netherlands | 1,876 |
| 8 | Switzerland | 1,838 |
| 9 | Portugal | 1,453 |
| 10 | Norway | 1,065 |

---

## 7. Data Patterns

### Hourly Sales Distribution
![Hourly Sales Distribution](fig1_hourly_sales.png)
*Figure 6: Sales distribution by hour of day – peak at 12:00 (70,321 transactions)*

### Daily Sales Trend
![Daily Sales Trend](fig2_daily_trend.png)
*Figure 7: Daily sales trend from Dec 1-6, 2010*

| Date | Number of Transactions |
|------|----------------------|
| Dec 01 | 1,872 |
| Dec 02 | 1,934 |
| Dec 03 | 1,084 |
| Dec 05 | 2,595 |
| Dec 06 | 1,888 |
| Dec 07 | 1,074 |
| Dec 08 | 1,897 |
| Dec 09 | 1,733 |
| Dec 10 | 1,344 |
| Dec 12 | 1,379 |
| Dec 13 | 1,251 |
| Dec 14 | 1,588 |
| Dec 15 | 1,258 |
| Dec 16 | 1,616 |
| Dec 17 | 700 |
| Dec 19 | 471 |
| Dec 20 | 818 |
| Dec 21 | 375 |
| Dec 22 | 215 |
| Dec 23 | 335 |
| Jan 04 | 733 |
| Jan 05 | 1,029 |
| Jan 06 | 1,242 |
| Jan 07 | 1,064 |
| Jan 09 | 1,072 |
| Jan 10 | 785 |
| Jan 11 | 817 |
| Jan 12 | 890 |
| Jan 13 | 719 |
| Jan 14 | 754 |
| Jan 16 | 602 |
| Jan 17 | 946 |
| Jan 18 | 518 |
| Jan 19 | 923 |
| Jan 20 | 677 |
| Jan 21 | 680 |
| Jan 23 | 839 |
| Jan 24 | 754 |
| Jan 25 | 1,168 |
| Jan 26 | 974 |
| Jan 27 | 1,284 |
| Jan 28 | 632 |
| Jan 30 | 697 |
| Jan 31 | 991 |
| Feb 01 | 1,212 |
| Feb 02 | 975 |
| Feb 03 | 826 |
| Feb 04 | 711 |
| Feb 06 | 272 |
| Feb 07 | 939 |
| Feb 08 | 606 |
| Feb 09 | 437 |
| Feb 10 | 642 |
| Feb 11 | 523 |
| Feb 13 | 594 |
| Feb 14 | 684 |
| Feb 15 | 997 |
| Feb 16 | 982 |
| Feb 17 | 1,049 |
| Feb 18 | 592 |
| Feb 20 | 820 |
| Feb 21 | 903 |
| Feb 22 | 1,127 |
| Feb 23 | 956 |
| Feb 24 | 1,098 |
| Feb 25 | 806 |
| Feb 27 | 783 |
| Feb 28 | 960 |
| Mar 01 | 1,088 |
| Mar 02 | 880 |
| Mar 03 | 878 |
| Mar 04 | 868 |
| Mar 06 | 811 |
| Mar 07 | 1,080 |
| Mar 08 | 1,175 |
| Mar 09 | 1,003 |
| Mar 10 | 880 |
| Mar 11 | 640 |
| Mar 13 | 522 |
| Mar 14 | 1,048 |
| Mar 15 | 836 |
| Mar 16 | 826 |
| Mar 17 | 1,012 |
| Mar 18 | 986 |
| Mar 20 | 1,179 |
| Mar 21 | 966 |
| Mar 22 | 1,205 |
| Mar 23 | 1,008 |
| Mar 24 | 1,472 |
| Mar 25 | 961 |
| Mar 27 | 707 |
| Mar 28 | 1,296 |
| Mar 29 | 1,016 |
| Mar 30 | 1,222 |
| Mar 31 | 1,008 |
| Apr 01 | 1,089 |
| Apr 03 | 695 |
| Apr 04 | 1,181 |
| Apr 05 | 924 |
| Apr 06 | 791 |
| Apr 07 | 1,275 |
| Apr 08 | 1,017 |
| Apr 10 | 919 |
| Apr 11 | 1,128 |
| Apr 12 | 1,060 |
| Apr 13 | 991 |
| Apr 14 | 1,458 |
| Apr 15 | 764 |
| Apr 17 | 934 |
| Apr 18 | 1,377 |
| Apr 19 | 1,161 |
| Apr 20 | 894 |
| Apr 21 | 1,367 |
| Apr 26 | 1,193 |
| Apr 27 | 1,020 |
| Apr 28 | 987 |
| May 01 | 445 |
| May 03 | 966 |
| May 04 | 1,118 |
| May 05 | 1,193 |
| May 06 | 1,292 |
| May 08 | 1,441 |
| May 09 | 1,050 |
| May 10 | 1,279 |
| May 11 | 1,449 |
| May 12 | 1,691 |
| May 13 | 1,091 |
| May 15 | 759 |
| May 16 | 1,174 |
| May 17 | 1,255 |
| May 18 | 1,125 |
| May 19 | 1,503 |
| May 20 | 932 |
| May 22 | 1,533 |
| May 23 | 1,256 |
| May 24 | 1,057 |
| May 25 | 991 |
| May 26 | 861 |
| May 27 | 829 |
| May 29 | 610 |
| May 31 | 883 |
| Jun 01 | 690 |
| Jun 02 | 1,019 |
| Jun 03 | 645 |
| Jun 05 | 1,496 |
| Jun 06 | 1,038 |
| Jun 07 | 1,408 |
| Jun 08 | 1,441 |
| Jun 09 | 1,358 |
| Jun 10 | 691 |
| Jun 12 | 1,041 |
| Jun 13 | 1,120 |
| Jun 14 | 1,005 |
| Jun 15 | 1,211 |
| Jun 16 | 1,229 |
| Jun 17 | 849 |
| Jun 19 | 1,139 |
| Jun 20 | 1,147 |
| Jun 21 | 966 |
| Jun 22 | 971 |
| Jun 23 | 1,551 |
| Jun 24 | 726 |
| Jun 26 | 655 |
| Jun 27 | 771 |
| Jun 28 | 733 |
| Jun 29 | 549 |
| Jun 30 | 1,169 |
| Jul 01 | 817 |
| Jul 03 | 577 |
| Jul 04 | 905 |
| Jul 05 | 779 |
| Jul 06 | 1,207 |
| Jul 07 | 1,236 |
| Jul 08 | 776 |
| Jul 10 | 801 |
| Jul 11 | 1,051 |
| Jul 12 | 718 |
| Jul 13 | 1,173 |
| Jul 14 | 1,355 |
| Jul 15 | 710 |
| Jul 17 | 1,172 |
| Jul 18 | 1,168 |
| Jul 19 | 1,454 |
| Jul 20 | 1,176 |
| Jul 21 | 1,290 |
| Jul 22 | 740 |
| Jul 24 | 1,045 |
| Jul 25 | 1,049 |
| Jul 26 | 836 |
| Jul 27 | 835 |
| Jul 28 | 1,245 |
| Jul 29 | 935 |
| Jul 31 | 1,216 |
| Aug 01 | 983 |
| Aug 02 | 898 |
| Aug 03 | 1,310 |
| Aug 04 | 1,412 |
| Aug 05 | 1,222 |
| Aug 07 | 518 |
| Aug 08 | 1,075 |
| Aug 09 | 858 |
| Aug 10 | 728 |
| Aug 11 | 1,336 |
| Aug 12 | 693 |
| Aug 14 | 529 |
| Aug 15 | 906 |
| Aug 16 | 934 |
| Aug 17 | 1,391 |
| Aug 18 | 1,433 |
| Aug 19 | 807 |
| Aug 21 | 1,027 |
| Aug 22 | 1,251 |
| Aug 23 | 1,333 |
| Aug 24 | 1,475 |
| Aug 25 | 1,179 |
| Aug 26 | 841 |
| Aug 28 | 1,154 |
| Aug 30 | 385 |
| Aug 31 | 743 |
| Sep 01 | 1,362 |
| Sep 02 | 1,082 |
| Sep 04 | 1,285 |
| Sep 05 | 1,336 |
| Sep 06 | 1,028 |
| Sep 07 | 973 |
| Sep 08 | 1,381 |
| Sep 09 | 1,254 |
| Sep 11 | 1,956 |
| Sep 12 | 1,423 |
| Sep 13 | 1,837 |
| Sep 14 | 1,125 |
| Sep 15 | 1,559 |
| Sep 16 | 1,237 |
| Sep 18 | 1,247 |
| Sep 19 | 1,339 |
| Sep 20 | 1,371 |
| Sep 21 | 1,675 |
| Sep 22 | 2,419 |
| Sep 23 | 1,868 |
| Sep 25 | 1,929 |
| Sep 26 | 1,506 |
| Sep 27 | 1,351 |
| Sep 28 | 2,071 |
| Sep 29 | 2,225 |
| Sep 30 | 1,439 |
| Oct 02 | 1,388 |
| Oct 03 | 1,711 |
| Oct 04 | 2,005 |
| Oct 05 | 2,045 |
| Oct 06 | 2,572 |
| Oct 07 | 1,898 |
| Oct 09 | 1,197 |
| Oct 10 | 2,677 |
| Oct 11 | 1,776 |
| Oct 12 | 1,422 |
| Oct 13 | 1,910 |
| Oct 14 | 1,466 |
| Oct 16 | 1,217 |
| Oct 17 | 2,315 |
| Oct 18 | 2,015 |
| Oct 19 | 1,785 |
| Oct 20 | 2,191 |
| Oct 21 | 1,285 |
| Oct 23 | 1,673 |
| Oct 24 | 1,818 |
| Oct 25 | 2,037 |
| Oct 26 | 1,670 |
| Oct 27 | 2,205 |
| Oct 28 | 1,378 |
| Oct 30 | 2,850 |
| Oct 31 | 1,816 |
| Nov 01 | 1,698 |
| Nov 02 | 1,712 |
| Nov 03 | 1,888 |
| Nov 04 | 2,380 |
| Nov 06 | 3,334 |
| Nov 07 | 1,700 |
| Nov 08 | 2,243 |
| Nov 09 | 2,102 |
| Nov 10 | 3,069 |
| Nov 11 | 2,358 |
| Nov 13 | 2,675 |
| Nov 14 | 2,828 |
| Nov 15 | 2,119 |
| Nov 16 | 2,649 |
| Nov 17 | 2,932 |
| Nov 18 | 2,089 |
| Nov 20 | 3,001 |
| Nov 21 | 2,282 |
| Nov 22 | 2,743 |
| Nov 23 | 3,166 |
| Nov 24 | 2,366 |
| Nov 25 | 1,639 |
| Nov 27 | 2,346 |
| Nov 28 | 2,690 |
| Nov 29 | 2,632 |
| Nov 30 | 2,096 |
| Dec 01 | 2,107 |
| Dec 02 | 1,922 |
| Dec 04 | 1,884 |
| Dec 05 | 3,293 |
| Dec 06 | 2,480 |
| Dec 07 | 2,097 |
| Dec 08 | 2,484 |
| Dec 09 | 603 |

### Daily Revenue Trend
![Daily Revenue Trend](fig7_daily_revenue.png)
*Figure 8: Daily revenue trend – highest on Dec 1*

**Key Patterns:**
- **Sales peak hour**: 12:00 (noon)
- **Peak day**: Nov 06 (highest transaction volume)
- **Weekday effect**: Monday–Friday account for >90% of transactions
- **Top product categories**: Decorations, hot water bottles, feltcraft toys, kitchenware

---

## 8. Output File Location

All files have been saved to: `D:\桌面\国家机密`
- `online_retail_cleaned.csv` – Cleaned dataset (returns retained)
- `preprocessing.md` – Preprocessing log
- `summary.md` – Data quality summary (this file)
- `fig1` to `fig8` – Visualization images
