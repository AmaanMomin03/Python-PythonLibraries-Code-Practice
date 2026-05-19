'''
Context:
StationeryBazaar, an online stationery retailer, is running a promotional campaign that offers a 20% discount. 
However, products priced below ₹50 after the discount should not be listed. 
The pricing team needs a rule-based automation to filter such products. 
Tasks: 
1. Apply a 20% discount to all products. 
2. Remove items that fall below ₹50 post-discount. 
3. Return the updated product-price dictionary. 
Sample Input: {'Pen': 60, 'Notebook': 120, 'Bag': 200} 
Expected Output: {'Notebook': 96.0, 'Bag': 160.0} 
'''

products =  {
    'Pen': 60, 
    'Notebook': 120, 
    'Bag': 200
    }

discount_dict = {}

for item,price in products.items():
    
    # Using 0.8 because 100*0.8 = 80
    discount = price * 0.8
    
    if discount >=50:
        discount_dict[item] = discount
print(discount_dict)
    


    

