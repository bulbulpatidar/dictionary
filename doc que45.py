l= [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000','color': 'Maroon'}, 
{'id': '#FFFF00', 'color': 'Yellow'},{'id': '#808000', 'color': 'Olive'}]
l2 = []
for i in l:
    if (i['id'] != '#FF0000'):
        l2.append(i)
print(l2)
    