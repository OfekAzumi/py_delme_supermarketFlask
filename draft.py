market = [
    {"name": "milk", "price": 2.99},
    {"name": "banana", "price": 0.79},
    {"name": "apple", "price": 1.29},
    {"name": "water", "price": 7.99},
    {"name": "beef", "price": 7.99},
    {"name": "bread", "price": 2.49},
    {"name": "eggs", "price": 1.99}
]

cart = [
    {"name": "milk", "price": 2.99},
    {"name": "banana", "price": 0.79},
    {"name": "apple", "price": 1.29},
    {"name": "milk", "price": 2.29},
    {"name": "water", "price": 1.29},
    {"name": "milk", "price": 2.29},
    {"name": "water", "price": 1.29}

]


def mergeDuplicates(arr):
    c1=0
    c2=0
    c3=0
    c4=0
    c5=0
    c6=0
    c7 = 0
    finalCart = []
    for prd in arr:
        if prd["name"] == "milk": c1+=1
        if prd["name"] == "banana": c2+=1
        if prd["name"] == "apple": c3+=1
        if prd["name"] == "water": c4+=1
        if prd["name"] == "beef": c5+=1
        if prd["name"] == "bread": c6+=1
        if prd["name"] == "eggs": c7+=1
    for prd in market:
        if prd["name"] == "milk": 
            if c1 > 0: finalCart.append({"name": "milk", "price": (c1*prd["price"])})
        if prd["name"] == "banana": 
            if c2 > 0: finalCart.append({"name": "banana", "price": (c2*prd["price"])})
        if prd["name"] == "apple":
            if c3 > 0: finalCart.append({"name": "banana", "price": (c3*prd["price"])})
        if prd["name"] == "water":
            if c4 > 0: finalCart.append({"name": "water", "price": (c4*prd["price"])})
        if prd["name"] == "beef":
            if c5 > 0: finalCart.append({"name": "beef", "price": (c5*prd["price"])})
        if prd["name"] == "bread":
            if c6 > 0: finalCart.append({"name": "bread", "price": (c6*prd["price"])})
        if prd["name"] == "eggs":
            if c7 > 0: finalCart.append({"name": "eggs", "price": (c7*prd["price"])})
    return finalCart
        
# def mergeDuplicated(arr):
#     tmp = arr
#     final = []
#     while tmp:
#         i = 0
#         pName = tmp[i]["name"]
#         pPrice = tmp[i]["price"]
#         c = 0
#         for x in tmp:
#             if pName == x["name"]: 
#                 if len(tmp) == 1: 
#                     c+=1
#                     final.append({"name": pName, "price": (c*pPrice)})
#                     return final
#                 else:
#                     tmp.remove(x)
#                     c+=1
#         final.append({"name": pName, "price": (c*pPrice)})
#     return final

name = 'milk'
price = 2.99
cart = []
cart.append({f'name : {name} , price : {price}, quan : {1}'}) #add new product to cart
print(cart)
print(market)