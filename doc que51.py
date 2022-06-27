even={'V': [1,5,9,8], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
dic={}
for i in even:
    a=[]
    for j in even[i]:
        if j%2==0:
            a.append(j)
        dic.update({i:a})        
          
print(dic)            


