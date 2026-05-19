'''
Context: 
EduSprint tracks student performance using exam scores. 
The academic team wants to identify top scorers, 
filter out high performers, 
and understand how they perform relative to others using statistical metrics. 

Tasks: 
1. Create a NumPy array from the score list. 
2. Sort scores in descending order. 
3. Return scores above 75. 
4. Calculate the average of those high scores. 

Sample Input: [65, 78, 82, 49, 91, 74] 

Expected Output: 
• Descending: [91, 82, 78, 74, 65, 49] 
• Scores > 75: [78, 82, 91] 
• Average: 83.67 

'''

import numpy as np

scores = [65, 78, 82, 49, 91, 74]

# Converting into numpy array
marks = np.array(scores)

# Sorting scores in decending order
dec_marks = np.sort(marks)[::-1]
print("Sorted Marks in Decending order:",dec_marks)

# Return scores above 75.
higher_range  = marks[marks > 75]
print("Printing marks above 75:",higher_range)

# Finding average
average = np.mean(higher_range)
print("Average:", round(average, 2))


