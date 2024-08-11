import olap.xmla.xmla as xmla

# Define Mondrian server connection parameters
mondrian_url = "http://localhost:8080/mondrian/xmla"
mondrian_catalog = "YourCatalogName"
mondrian_cube = "YourCubeName"

# Connect to Mondrian server
conn = xmla.XMLAProvider().connect(mondrian_url)

# Create MDX query to retrieve data
mdx_query = """
SELECT
  [Measures].[Sales] ON COLUMNS,
  [Product].[Category].Members ON ROWS
FROM
  [{}]
""".format(mondrian_cube)

# Execute MDX query and fetch results
result = conn.Execute(mondrian_catalog, mdx_query)
data = result.getSlice()

# Convert result to pandas DataFrame
import pandas as pd
df = pd.DataFrame(data, columns=['Category', 'Sales'])

# Plotting using Matplotlib
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.bar(df['Category'], df['Sales'])
plt.xlabel('Category')
plt.ylabel('Sales')
plt.title('Sales by Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
