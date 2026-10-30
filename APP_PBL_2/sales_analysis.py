import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Read CSV file
file_path = os.path.join(os.path.dirname(__file__), "monthly_sales.csv")
df = pd.read_csv(file_path)

print("SALES DATA")
print(df)

# 2. Display total sales and average sales
total_sales = df["Sales"].sum()
average_sales = df["Sales"].mean()

print("\nTotal Sales:", total_sales)
print("Average Sales:", average_sales)

# 3. Identify month with highest sales
monthly_sales = df.groupby("Month")["Sales"].sum()

highest_month = monthly_sales.idxmax()

print("\nMonth with Highest Sales:", highest_month)
print("Highest Sales:", monthly_sales.max())

# 4. Group sales by product category
category_sales = df.groupby("Product_Category")["Sales"].sum()

print("\nSales by Product Category:")
print(category_sales)

# 5. Bar chart comparing sales by category
plt.figure()
plt.bar(category_sales.index, category_sales.values)
plt.title("Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.show()

# 6. Line chart showing monthly sales trends
plt.figure()
plt.plot(monthly_sales.index, monthly_sales.values, marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid()
plt.show()

# 7. Pie chart showing category contribution
plt.figure()
plt.pie(category_sales.values,
        labels=category_sales.index,
        autopct="%1.1f%%")
plt.title("Sales Contribution by Category")
plt.show()

# Conclusion
print("\nSales Data Analysis Completed Successfully!")