'''
Context: 
SwiftMart operates in multiple regions and wants to understand which zones are placing the most product orders. 
The operations team needs to analyze quantities sold per region and prioritize logistics accordingly. 

Tasks: 
1. Create a DataFrame using the following data: 
o region: ['East', 'West', 'East', 'North', 'West'] 
o item: ['Pen', 'Pen', 'Notebook', 'Pencil', 'Notebook'] 
o quantity: [10, 3, 6, 2, 7]

2. Filter orders where quantity > 5. 
3. Group by region and calculate total quantity.
4. Sort regions by total quantity. 

Expected Output: 
region total_quantity
East   16
West   10
'''
import pandas as pd

data_frame = {
    
    'region': ['East', 'West', 'East', 'North', 'West'],
    'item' : ['Pen', 'Pen', 'Notebook', 'Pencil', 'Notebook'],
    'quantity' : [10, 3, 6, 2, 7]   
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data_frame)
print("Converted Dictionary into Dataframe:\n",df)


filter_orders = df[df['quantity'] > 5]
print("\nFilter the orders :",filter_orders)

# Group by region and calculate total quantity.
groupping_region = filter_orders.groupby('region')['quantity'].sum()
print("\noupping th esame region:\n",groupping_region)

