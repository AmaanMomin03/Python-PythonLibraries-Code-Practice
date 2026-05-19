'''
Context: 
ShopEase is an e-commerce company analyzing customer search trends. 
Due to repeated and inconsistent entries of product names, 
the dataset is messy and requires preprocessing for better analysis and visualization.
 
Tasks: 
1. Remove duplicates and sort product names alphabetically. 
2. Convert the sorted list to a set. 
3. Check if 'mobile' is in the set. 

Sample Input: ["laptop", "mobile", "tablet", "mobile", "laptop"] 

Expected Output: 
• Sorted List: ['laptop', 'mobile', 'tablet'] 
• Set: {'mobile', 'tablet', 'laptop'} 
• Contains 'mobile': True 

'''

product = ["laptop", "mobile", "tablet", "mobile", "laptop"]

# Sorted  the list
product.sort()
print("Sorted list:",product)

og_product = list(set(product))
print("Original Sorted List:",og_product)

# og_product_set = set(map(lambda i,j : (i,j), og_product ))
og_product_set = set(og_product)
print("Original product into set:", og_product_set)

# if 'mobile' == og_product:
#     print(True)
print("mobile" in og_product_set)