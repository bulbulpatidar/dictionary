d1={2:200,3:300}
d2={4:400,5:500,6:600}
d={}
for i in (d1,d2):
    d.update(i)
print(d)    
