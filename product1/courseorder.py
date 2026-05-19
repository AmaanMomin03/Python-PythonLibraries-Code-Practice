'''
Dataset: The list contains course names in arbitrary order, possibly with duplicates. Tasks: 

1. Remove duplicate course names and return a list of unique course names sorted alphabetically. 
2. Create a dictionary that maps each unique course to a standardized course code, starting from "C101". 
3. Return the total count of unique courses. 
Sample Input: courses = ["", "ML", "DS", "ML", ""]
 
Expected Output: 
• Sorted: ['DS', 'ML', '']
• Mapping: {'DS': 'C101', 'ML': 'C102', '': 'C103'} 
• Total: 3 

Sample Input: courses = ["AI", "Cyber Security", "Data Science", "AI", "Blockchain", "Data Science"] Expected Output: 
• Sorted: ['AI', 'Blockchain', 'Cyber Security', 'Data Science'] • Mapping: {'AI': 'C101', 'Blockchain': 'C102', 'Cyber Security': 'C103', 'Data Science': 'C104'} 
• Total: 4 
'''

# Initializing list
course = ["", "ML", "DS", "ML", ""]

# Initializing Values
course_number = ['C101', 'C102', 'C103']


# Removing duplicates from the list
unique_course = list(set(course))
print(unique_course)

# Sorting in alphabetical order
unique_course.sort()
print(unique_course)

# Finding the count pf the courses
count = len(unique_course)
print(count)

mapping = map(str.lower, course)
print(list(mapping))


#  Printing original keys-value lists
print("original key list is : " + str(course))
print("original value list is : " + str(course_number))

# using map and dict type casting
# to convert lists to dictionary

result = dict(map(lambda i,j : (i,j) , course, course_number))
print("Dictionary for unique corses :" ,result)






