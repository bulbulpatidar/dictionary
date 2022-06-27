# Q46.Write a Python program to convert string values of a given dictionary, into integer/float
# datatypes. Go to the editor
# Original list:
# [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# String values of a given dictionary, into integer types:
# [{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]
# Original list:
# [{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
# String values of a given dictionary, into float types:
# [{'x': 10.12, 'y': 20.23, 'z': 30.0}, {'p': 40.0, 'q': 50.19, 'r': 60.99}]
dic= [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
c={}
d={}
for i in dic:
    for j in i:
        for k in dic[0]:
            d.update({k:int(i[k])})
            print(k)
            # c.update({j:int(i[j])})
# print(c) 
print(d)     jnkkk




