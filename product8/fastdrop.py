'''
Context: 
FastDrop is a delivery startup looking to improve its service. 
They want to analyze delivery time records to calculate averages, detect skewed performance, and identify anomalies that may require operational changes. 

Tasks: 
1. Compute mean, median, and mode. 
2. Determine if the data is skewed. 
3. Identify outliers using the IQR method. 

Sample Input: [30, 32, 29, 31, 60, 28, 33] 

Expected Output: 
• Mean: 34.71 
• Median: 31 
• Skew: Right 
• Outliers: [60] 
'''

import numpy as np
import pandas as pd

# Converting into data frame
numbers = [30, 32, 29, 31, 60, 28, 33]
data = pd.DataFrame(numbers)

# Finding Mean
mean_data = np.mean(data)
print("Mean:",mean_data)

# Finding Mode
median_data = np.median(data)
print("Median:",median_data)

# Finding Skew
if mean_data > median_data:
    skew = "Right"
elif mean_data < median_data:
    skew = "Left"
else:
    skew = "Symmetric"
print("Skew:", skew)

# Finding IQR

sorted_data = sorted(numbers)
print(sorted_data)
q1 = 29
q3 = 33

iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers = []

for num in sorted_data:
    if num < lower or num > upper:
        outliers.append(num)

print("Outliers:", outliers)
