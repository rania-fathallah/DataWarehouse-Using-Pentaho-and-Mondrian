import pandas as pd

# Read the CSV file into a DataFrame
df1 = pd.read_csv("./data_1.csv")
df2 = pd.read_csv("./data_2.csv")

# Display the first few rows of the DataFrame
print("DF1:",end="\n\n")
print(df1.head(),end="\n\n\n")
print("DF2:",end="\n\n")
print(df2.head(),end="\n\n\n")

# Display data properties
print("Data properties:")
print("DF1:",end="\n\n")
print(df1.describe(),end="\n\n\n")
print("DF2:",end="\n\n")
print(df2.describe(),end="\n\n\n")

# Count the number of null values in each column
print("Number of null values in each column:")
print("DF1:",end="\n\n")
print(df1.isnull().sum(),end="\n\n\n")
print("DF2:",end="\n\n")
print(df2.isnull().sum())