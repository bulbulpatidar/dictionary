d={'Cierra Vega': 12, 'Alden Cantrell': 14, 'Kierra Gentry': 12, 'Pierre Cox': 12}
for i in d:
    a=d[i]
    c=0
    for j in d:
        if d[j]==a:
            c+=1
# print(c)  
if c==len(d):
    print("true")
else:
    print("false")              


    