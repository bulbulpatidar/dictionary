l=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},
{"V":"S009"},{"VIII":"S007"}]  
a=[]
for i in l:
    for j in i:
        if i[j] not in a:
            a.append(i[j])  
print(set(a))
              

   