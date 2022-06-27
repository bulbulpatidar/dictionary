
my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for i in my_dict:
    print(i,end=" ")
print()
l1=list(my_dict.values())
# print(l1)
for i in range(len(l1)):
    # print(i)
    for j in range(len(l1)):
        d=l1[j][i]
        print(d,end="  ")
    print()            

