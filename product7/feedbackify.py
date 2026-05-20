'''
Context: 
Feedbackify collects customer reviews, but many user names are inconsistent due to case issues and extra spaces. 
The data team wants to clean and deduplicate names while performing a basic analysis on how many users fall under specific patterns. 

Tasks: 
1. Strip whitespace and convert each name to title case.
2. Remove duplicates while preserving order. 
3. Count how many names start with 'A'. S

ample Input: [" alice ", "Bob", "ALICE", "Adam", "bob"] 

Expected Output: 
• Cleaned: ['Alice', 'Bob', 'Adam'] 
• Count of 'A': 2
'''

names = [" alice ", "Bob", "ALICE", "Adam", "bob"]

cleaned = []

count = 0

# Converting names into Proper title
for name in names:
    cleaned.append(name.strip().title())
print("Cleaned Data:",cleaned)

# Now removing duplicates
rmv_dup = list(set(cleaned))
print("After removing Dublicates:",rmv_dup)

# Count how many names start with 'A'. S

for name in rmv_dup:
    if name.startswith('A'):
        count += 1
print("Count of A:",count)




