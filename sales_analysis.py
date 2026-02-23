import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\Admin\Desktop\superstore.csv")

# Convert Order.Date to datetime
df['Order.Date'] = pd.to_datetime(df['Order.Date'])

# Drop unnecessary column
df = df.drop(columns=['记录数'])

# =========================
# 1️⃣ Total Sales & Profit
# =========================

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)

# =========================
# 2️⃣ Sales by Category
# =========================

category_sales = df.groupby('Category')['Sales'].sum()
print("\nSales by Category:\n", category_sales)

category_sales.plot(kind='bar')
plt.title("Sales by Category")
plt.ylabel("Sales")
plt.show()

# =========================
# 3️⃣ Region-wise Sales
# =========================

region_sales = df.groupby('Region')['Sales'].sum()
print("\nSales by Region:\n", region_sales)

region_sales.plot(kind='bar')
plt.title("Sales by Region")
plt.ylabel("Sales")
plt.show()

# =========================
# 4️⃣ Monthly Sales Trend
# =========================

df['Month'] = df['Order.Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()

monthly_sales.plot(kind='line')
plt.title("Monthly Sales Trend")
plt.xticks(rotation=45)
plt.show()

top_products = df.groupby('Product.Name')['Sales'].sum().sort_values(ascending=False).head(5)

print("\nTop 5 Products by Sales:\n", top_products)

top_products.plot(kind='bar')
plt.title("Top 5 Products by Sales")
plt.ylabel("Sales")
plt.xticks(rotation=45)   # 👈 Add this line
plt.tight_layout()        # 👈 Add this line (very important)
plt.show()

segment_profit = df.groupby('Segment')['Profit'].sum()

print("\nProfit by Segment:\n", segment_profit)

print("\nHighest Profit Segment:", segment_profit.idxmax())

segment_profit.plot(kind='bar')
plt.title("Profit by Segment")
plt.ylabel("Profit")
plt.show()

category_profit = df.groupby('Category')['Profit'].sum()

print("\nProfit by Category:\n", category_profit)

category_profit.plot(kind='bar')
plt.title("Profit by Category")
plt.ylabel("Profit")
plt.show()