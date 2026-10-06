import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------
# 1. Load the dataset
# -------------------------

df = pd.read_csv("product_sales.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

print("Dataset loaded successfully!\n")


# -------------------------
# 2. Understand the data
# -------------------------

print("First 5 rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nDataset information:")
df.info()

print("\nStatistical summary:")
print(df.describe())


# -------------------------
# 3. Check missing values
# -------------------------

print("\nMissing values:")
print(df.isnull().sum())


# -------------------------
# 4. Select Product A
# -------------------------

product_a = df[df["Product"] == "Product A"]

print("\nProduct A data:")
print(product_a.head())


# -------------------------
# 5. Sales Trend
# -------------------------

plt.figure(figsize=(12, 6))

sns.lineplot(
    data=product_a,
    x="Date",
    y="Units_Sold",
    marker="o"
)

plt.title("Product A Sales Trend")
plt.xlabel("Date")
plt.ylabel("Units Sold")

plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()


# -------------------------
# 6. Price vs Sales
# -------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=product_a,
    x="Price",
    y="Units_Sold",
    s=100
)

plt.title("Price vs Units Sold - Product A")
plt.xlabel("Price")
plt.ylabel("Units Sold")

plt.grid(True)
plt.show()


# -------------------------
# 7. Marketing Spend vs Sales
# -------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=product_a,
    x="Marketing_Spend",
    y="Units_Sold",
    s=100
)

plt.title("Marketing Spend vs Units Sold - Product A")
plt.xlabel("Marketing Spend")
plt.ylabel("Units Sold")

plt.grid(True)
plt.show()


# -------------------------
# 8. Rating vs Sales
# -------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=product_a,
    x="Rating",
    y="Units_Sold",
    s=100
)

plt.title("Customer Rating vs Units Sold - Product A")
plt.xlabel("Customer Rating")
plt.ylabel("Units Sold")

plt.grid(True)
plt.show()


# -------------------------
# 9. Our Price vs Competitor Price
# -------------------------

plt.figure(figsize=(12, 6))

plt.plot(
    product_a["Date"],
    product_a["Price"],
    marker="o",
    label="Our Price"
)

plt.plot(
    product_a["Date"],
    product_a["Competitor_Price"],
    marker="o",
    label="Competitor Price"
)

plt.title("Our Price vs Competitor Price")
plt.xlabel("Date")
plt.ylabel("Price")

plt.legend()
plt.grid(True)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# -------------------------
# 10. Stock Availability vs Sales
# -------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=product_a,
    x="Stock_Availability",
    y="Units_Sold",
    s=100
)

plt.title("Stock Availability vs Units Sold")
plt.xlabel("Stock Availability (%)")
plt.ylabel("Units Sold")

plt.grid(True)
plt.show()


# -------------------------
# 11. Sales by Region
# -------------------------

region_sales = product_a.groupby("Region")["Units_Sold"].sum()

print("\nTotal sales by region:")
print(region_sales)

plt.figure(figsize=(8, 5))

region_sales.plot(
    kind="bar"
)

plt.title("Product A Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Units Sold")

plt.xticks(rotation=0)
plt.grid(axis="y")

plt.tight_layout()
plt.show()


# -------------------------
# 12. Correlation Matrix
# -------------------------

correlation = product_a.corr(numeric_only=True)

print("\nCorrelation Matrix:")
print(correlation)


# -------------------------
# 13. Correlation Heatmap
# -------------------------

plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Product A Correlation Heatmap")

plt.tight_layout()
plt.show()
