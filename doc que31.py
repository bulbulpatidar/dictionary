
d={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55,'item5': 24}
top1=0
top2=0
top3=0
for i in d:
    for j in d:
        if d[j]>top1:
            top1=d[j]
            a=j
        if d[j]>top2 and d[j]!=top1:
            top2=d[j]
            b=j
        if d[j]>top3 and d[j]!=top1 and d[j]!=top2:
            top3=d[j]
            c=j
print(a,top1)
print(b,top2)
print(c,top3)                   
