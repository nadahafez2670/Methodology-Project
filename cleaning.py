import pandas as pd
import re

df = pd.read_csv("Final_Data.csv")

print(df.head())
print(df.tail())
print(df.info())          
print(df.columns)              
print(df.describe()) 
print(df.isnull().sum()) 
duplicates = df.duplicated().sum()
print(f"Number of duplicates: {duplicates}")

# Product_Name
df["Product_Name"] = (
    df["Product_Name"]
    .str.replace("\n", " ", regex=False)
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
    .astype('string') 
)

# Price
df['Price'] = (
    df['Price']
    .str.replace('EGP', '', regex=False)
    .str.replace('\n', '.', regex=False)
    .str.replace(',', '', regex=False)
    .str.strip()
    .astype(float)
)

# Pre_price
df['Pre_price'] = (
    df['Pre_price']
    .str.replace('EGP', '', regex=False)
    .str.replace('\n', '.', regex=False)
    .str.replace(',', '', regex=False)
    .str.strip()
    .astype(float)
)

# Monthly_Purchases
def extract_purchases(x):
    if isinstance(x, str):
        # لو فيها K
        if 'K' in x:
            num = re.findall(r'\d+', x)
            if num:
                return int(num[0]) * 1000
        # لو رقم عادي
        num = re.findall(r'\d+', x)
        if num:
            return int(num[0])
    return None  # قيم ملهاش علاقة بالشراء

df['Monthly_Purchases'] = df['Monthly_Purchases'].apply(extract_purchases)
df['Monthly_Purchases'] = df['Monthly_Purchases'].astype('float')


# Ratings
df['Ratings'] = df['Ratings'].fillna(0)

# Brand
df['Brand'] = df['Brand'].str.strip().astype('string')

df = df.dropna(subset=['Price', 'Monthly_Purchases'])
df['Monthly_Purchases'] = df['Monthly_Purchases'].astype('int64')
df = df.drop(columns=['Pre_price'])
df = df.drop_duplicates()

print(df.head())
print(df.tail())
print(df.info())          
print(df.columns)              
print(df.describe()) 
print(df.isnull().sum()) 
duplicates = df.duplicated().sum()
print(f"Number of duplicates: {duplicates}")



df.to_csv("Cleaned_Data.csv", index=False)


















    






