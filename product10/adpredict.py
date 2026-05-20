'''
Context: 
AdPredict uses age data to target ads. 
They need to segment potential customers based on age ranges, analyze demographics above the average age, 
and ensure no duplicates skew the insights. 

Tasks: 
1. Return all ages between 18 and 25. 
2. Count how many are above the average age. 
3. Remove duplicate ages from the list. 

Sample Input: [17, 22, 21, 19, 22, 30, 25, 21] 

Expected Output: 
• Ages 18–25: [22, 21, 19, 22, 25, 21] 
• Average: 22.125 → Count above avg: 2 
• Unique: [17, 22, 21, 19, 30, 25] 
'''

ages = [17, 22, 21, 19, 22, 30, 25, 21] 

# Sorting age
sorted_ages = sorted(ages)
print("Sorted Age:",sorted_ages)

# Return all ages between 18 and 25.
age_range = []
for age in sorted_ages:
    if 18 <= age <= 25:
        age_range.append(age)
print("Ages between 18 to 25:",age_range)

# Count how many are above the average age.
count = 0
average_ages = sum(sorted_ages) / len(sorted_ages)
print("Average of ages:",average_ages)

for age in sorted_ages:
    if age > average_ages:
        count +=1
print("Count above avg:", count)

# Remove duplicate ages from the list.
rmv_dublicats = list(set(sorted_ages))
print("Removing duplicate ages from the list:",rmv_dublicats)
        



