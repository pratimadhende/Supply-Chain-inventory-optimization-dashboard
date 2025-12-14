# -----------------
# import libraries
# -----------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# -------------
# Load dataset
# -------------
df=pd.read_csv("supply_chain_data.csv")
print(df.head())
print(df.info())
# ----------------
# Clean the data
# ----------------
df.drop_duplicates(inplace=True)
df.fillna(0,inplace=True)
# --------------------
# Inventory analysis
# --------------------
# Inventory turnover ratio
df["Inventory_Turnover"]=df["Number of products sold"] / df["Stock levels"]

# Stock status (Over / Under stock)
df["Stock_Status"]=np.where(df["Stock levels"]<df["Number of products sold"],"Understock","Overstock")
# -----------------------------
# Supplier lead time analysis
# -----------------------------
supplier_lead_time=df.groupby("Supplier name")["Lead times"].mean()
print(supplier_lead_time.sort_values(ascending=False))
# ----------------
# Visualizations
# ----------------
# Stock Level Distributuion
plt.hist(df["Stock levels"])
plt.title("Stock Level Distributuion")
plt.xlabel("Stock Levels")
plt.ylabel("Count")
plt.show()

# Demand vs Stock
plt.scatter(df["Number of products sold"], df["Stock levels"])
plt.xlabel("Product Sold")
plt.ylabel("Stock Levels")
plt.title("Demand vs Stock Analysis")
plt.show()

# Stock Status Count
df["Stock_Status"].value_counts().plot(kind="bar")
plt.title("Overstock vs Understock")
plt.xlabel("Stock Status")
plt.ylabel("Count")
plt.show()

# ------------------
# Export Clean Data
# ------------------
df.to_csv("clean_supply_chain.csv",index=False)
print("Clean data exported successfully")