'''
Context: FreshMart, a grocery chain, wants to understand regional product demand. 
The analytics team must summarize sales quantities by region, identify high-demand zones, and rank them for stock planning.

Tasks: 
1. Create a DataFrame using the data above. 
2. Filter rows where quantity > 6. 
3. Group by region and return total quantity. 
4. Sort by total quantity descending. 
'''
import pandas as pd
zone = {
    
    'region': ['East', 'West', 'East', 'North', 'West'],
    'item' : ['Apple', 'Banana', 'Carrot', 'Apple', 'Carrot'],
    'quantity' : [10, 3, 6, 2, 7]  
}

# Creating a DataFrame using the data above. 
data = pd.DataFrame(zone)
print("Dataframe:\n",data)

#  Filtering rows where quantity > 6.
# filter = []
# for i in filter:
#     if 'quantity' > 6:
#         filter.append(i)
#         i += 1
filter_qauntity = data[data['quantity'] > 6]
print("\nRows where quantity > 6:\n",filter_qauntity)

# Group by region and return total quantity.
group_region = data.groupby('region')['quantity'].sum()
print("\nGrouping by region and return total quantity:\n",group_region)

# Sort by total quantity descending.
sort_qauntity = group_region.sort_values(ascending=False)
print("\nSort by total quantity descending:\n",sort_qauntity)








