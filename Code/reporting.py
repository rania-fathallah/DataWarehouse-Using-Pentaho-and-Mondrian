import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Database connection parameters
db_params = {
    'host': 'localhost',
    'database': 'database_name',
    'user': 'username',
    'password': 'password'
}
engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}/{db_params["database"]}')

query = '''
    SELECT f.*, p.category
    FROM facttable f
    JOIN productdim p ON f.productid = p.productid
'''

df = pd.read_sql(query, engine)


# Perform reporting
total_sales_per_customer = df.groupby('customerid')['sales'].sum()

plt.figure(figsize=(10, 6))
sns.barplot(x=total_sales_per_customer.index, y=total_sales_per_customer.values)
plt.xlabel('CustomerID')
plt.ylabel('Total Sales')
plt.title('Total Sales per Customer')
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(df['profitratio'], bins=20, kde=True)
plt.xlabel('Profit Ratio')
plt.ylabel('Frequency')
plt.title('Profit Ratio Distribution')
plt.show()


plt.figure(figsize=(8, 6))
sns.scatterplot(x='sales', y='profit', data=df)
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.title('Profit vs. Sales')
plt.show()

plt.figure(figsize=(10, 6))
sales_by_category = df.groupby('category')['sales'].sum().sort_values(ascending=False)
sales_by_category.plot(kind='bar')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.title('Sales Distribution by Product Category')
plt.xticks(rotation=45)
plt.show()
