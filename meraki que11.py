my_dict = {'a':50, 'b':58, 'c':56,'d':40 ,'e':100, 'f':20}
l=0
l1=0
l2=0
m=[]
for i in my_dict:
    for j in my_dict:
        if my_dict[j]>l:
            l=my_dict[j]
        if my_dict[j]>l1 and my_dict[j]!=l:
            l1=my_dict[j]
        if my_dict[j]>l2 and my_dict[j]!=l and my_dict[j]!=l1:
            l2=my_dict[j]              
m.append(l)
m.append(l1)
m.append(l2)
print(m)