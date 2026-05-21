'''
Context: 
ZipLogistics is reviewing delivery times to improve logistics. 
The team wants to assess if delivery t imes are consistent or skewed, and identify any significant outliers using statistical methods. 

Data: [24, 30, 29, 31, 58, 28, 34] 

Tasks: 
1. Calculate the mean and median delivery time. 
2. Identify if the data is skewed (Left/Right/Normal). 
3. Remove outliers using the IQR method. 

'''
import numpy as np

values =  [24, 30, 29, 31, 58, 28, 34] 

# Calculate the mean and median delivery time.
mean_data = np.mean(values)
print("Mean Data:",mean_data)

median_data = np.median(values)
print("Median Data:",median_data)

# Identify if the data is skewed (Left/Right/Normal).
if mean_data > median_data:
    skew = "Right"
elif mean_data < median_data:
    skew = "Left"
else:
    skew = "Normal"
print("Skew:", skew)

# Remove outliers using the IQR method.
sorted_data = sorted(values)
print("Sorted Data:",sorted_data)
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

