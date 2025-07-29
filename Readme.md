## End to End Machine Learning - Sales Forecasting project using Superstore dataset

```text

We hav Superstore dataset with following columns

--------------------------------------------------------------------
--------------------------------------------------------------------
                            1. Basic EDA
--------------------------------------------------------------------
--------------------------------------------------------------------


<class 'pandas.core.frame.DataFrame'>
RangeIndex: 9994 entries, 0 to 9993
Data columns (total 21 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   Row ID         9994 non-null   int64  
 1   Order ID       9994 non-null   object 
 2   Order Date     9994 non-null   object 
 3   Ship Date      9994 non-null   object 
 4   Ship Mode      9994 non-null   object 
 5   Customer ID    9994 non-null   object 
 6   Customer Name  9994 non-null   object 
 7   Segment        9994 non-null   object 
 8   Country        9994 non-null   object 
 9   City           9994 non-null   object 
 10  State          9994 non-null   object 
 11  Postal Code    9994 non-null   int64  
 12  Region         9994 non-null   object 
 13  Product ID     9994 non-null   object 
 14  Category       9994 non-null   object 
 15  Sub-Category   9994 non-null   object 
 16  Product Name   9994 non-null   object 
 17  Sales          9994 non-null   float64
 18  Quantity       9994 non-null   int64  
 19  Discount       9994 non-null   float64
 20  Profit         9994 non-null   float64
dtypes: float64(3), int64(3), object(15)
memory usage: 1.6+ MB

-> We found that there is no missing value in data but Order Date and Ship Date is in Object format, we need to convert this into Datetime format

-> We data from January 2011 to December 2014.

-> We have checked duplicates in data, there is none.

-> We have checked the no. of unique values,

Row ID           9994
Order ID         5009
Order Date       1238
Ship Date        1334
Ship Mode           4
Customer ID       793
Customer Name     793
Segment             3
Country             1
City              531
State              49
Postal Code       631
Region              4
Product ID       1862
Category            3
Sub-Category       17
Product Name     1841
Sales            5825
Quantity           14
Discount           12
Profit           7287
Month              48

and found that,

There are 9,994 total transaction in 48 months, means in 4 years.
order id less than row id means there are multiple items in one order.
Orders dates are 1238 in 1440 days of 4 years, means 202 days have no orders.
Ship dates are 1334, more than order date, means one order may be shipped in multiple dates
We have 793 customers.
Country is one so this is only domestic sales data.
City count is more than 500, need to check if spelling error
City is 531 and postal code is 631, need to check
We have 1862 product id and 1841 product, some product may have same name but have different IDs.


Check unique values of each categorycal column,

Ship Mode has unique values: ['First Class' 'Standard Class' 'Second Class' 'Same Day']

Segment has unique values: ['Consumer' 'Home Office' 'Corporate']

Category has unique values: ['Furniture' 'Office Supplies' 'Technology']

Sub-Category has unique values: ['Bookcases' 'Tables' 'Paper' 'Phones' 'Chairs' 'Fasteners' 'Furnishings'
 'Storage' 'Labels' 'Binders' 'Appliances' 'Art' 'Accessories' 'Copiers'
 'Envelopes' 'Machines' 'Supplies']


We will use below features for our sales forecasting model becoz others are not useful,

['Category', 'Sub-Category', 'Segment', 'Region', 'Ship Mode'] as categorical features 

["Discount"] as numerical features

["Quantity"] as Target feature

```


```text


--------------------------------------------------------------------
--------------------------------------------------------------------
                            2. Outlier Detection
--------------------------------------------------------------------
--------------------------------------------------------------------


We have four numerical columns

num_cols = ["Sales", "Profit", "Quantity", "Discount"]

and among "Quantity is important as it is what we will predict

We used box plot to detects the outlier

```

<img width="800" height="400" alt="Quantity" src="https://github.com/user-attachments/assets/fe2ced20-f0c0-47a7-91a0-f138f89a1014" />

```text

Key Observations (Quantity) :
Median (middle line): Around 3–4 units.
Interquartile Range (IQR): Between 2 and 8 units.
Whiskers: Extend roughly from 1 to 9
Outliers: Values at 10, 11, 12, 13, and 14 are considered outliers (those beyond 1.5 * IQR from Q1 or Q3).

also we have count of outlier as below,

```

<img width="800" height="500" alt="outlier_counts" src="https://github.com/user-attachments/assets/35124c0b-32b1-439a-83bc-7bd51d0c43bc" />

```text

Quantity = 10 is the most frequent outlier with over 55 occurrences
Quantities 11–14 also appear frequently, though less than 10.
This suggests these aren't just rare data-entry errors — they're likely real business events.

This means 

Bulk Orders - Some customers may consistently purchase in larger quantities (10+), we need to check customer wise sales
Promotional Sales - Special offers or discounts encouraging higher quantity buys.
Seasonal Effects: Specific times (e.g., festivals or end of month) may trigger larger purchases.

due to this we capped the "Quantity" at 9

and create new feature as "high_qty" with two values - "Normal Order" and "High Qty Order"




```
