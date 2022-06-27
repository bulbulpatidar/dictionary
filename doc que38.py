dic={'c1': 'Red', 'c2': 'Green', 'c3': None}
x={}
for i,j in dic.items():
    if j!=None:
        x[i]=j
print(x)

