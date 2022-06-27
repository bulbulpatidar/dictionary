l=[{'item': 'item1', 'amount': 400}, 
{'item': 'item2', 'amount': 300}, 
{'item': 'item1','amount': 750}]
var={}
for i in l:
    if i["item"] not in var:
        var[i["item"]]=i["amount"]
    else:
        var[i["item"]]+=i["amount"]
print(var)        