d = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}
d1= {}
for i,j in d.items():
    # print(i,j)
    for x in " ":
        i = i.replace(x,"")
        d1[i]= j
        
print(d1)
