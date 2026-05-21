'''
Context: 
MarketTrack is creating a monthly performance dashboard. 
The marketing team wants a line chart of monthly sales with clear labels and visual highlights to easily identify performance trends. 

Tasks: 
1. Create a line plot using Matplotlib to display monthly sales. 
2. Add labels for the X-axis (Month) and Y-axis (Sales), and include a title. 
3. Highlight the highest sales month using a red marker

Sample Data: 
months = ['Jan','Feb', 'Mar, 'Apr', 'May', 'Jun']
sales = [12000, 15000, 18000, 14000, 20000, 17000]
'''
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [12000, 15000, 18000, 14000, 20000, 17000]

# Markers
plt.plot(months, sales, marker='o')

# Labels
plt.plot(months,sales)
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Simple Plot')

# Finding Highest sales
max_sales = max(sales)
max_index = sales.index(max_sales)

# Highlight highest month
plt.scatter(months[max_index], max_sales, color='red', s=100)

plt.show()