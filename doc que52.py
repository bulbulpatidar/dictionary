dic={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 200, 'g': 57, 'h': 8, 'i': 100}
l=[]
for i in dic:
    l.append(dic[i])
for j in range(0,len(l)):
    for k in range(0,len(l)):
        if l[j]>l[k]:
            l[j],l[k]=l[k],l[j]
# print(l)            
k=[]
for n in range(0,5):
    for m in dic:
        if l[n]==dic[m]:
            k.append(m)
print(k)            
