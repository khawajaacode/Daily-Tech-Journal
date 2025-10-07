import pandas as pd

# Load your dataset
df = pd.read_csv("data.csv")

# Show first 5 rows
print("Original Data:")
print(df.head())

# 1. Remove duplicate rows
df = df.drop_duplicates()

# 2. Handle missing values (fill with mean for numbers, mode for text)
for col in df.columns:
    if df[col].dtype == 'object':
        df[col].fillna(df[col].mode()[0], inplace=True)
    else:
        df[col].fillna(df[col].mean(), inplace=True)

# 3. Remove rows with all missing values
df = df.dropna(how='all')

# 4. Strip extra spaces in text columns
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# 5. Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned Data saved to cleaned_data.csv")
