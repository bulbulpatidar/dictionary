
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
a={}
for i in (d1,d2):
    a.update(i)
for i in a:
    if i in d1:
        if i in d2:
            a.update({i:d1[i]+d2[i]})
print(a)            

       
