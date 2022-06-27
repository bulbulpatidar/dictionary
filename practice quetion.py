# a=[1,2,3,4,5,1,1,2,2,3]
# i=0
# dic={}
# while i<len(a):
#     j=0
#     c=0
#     while j<len(a):
#         if a[i]==a[j]:
#             c+=1
#         j+=1
#     dic.update({a[i]:c})
#     i+=1
# print(dic)    
               
# dic={2:20,4:40,5:50,6:60}
# n=int(input("enter the key:-"))
# if n in dic:
#     dic.pop(n)
#     print(dic)
# else:
#     v=int(input("enter the value:-"))
#     dic[n]=v
#     print(dic) 
# 
# a={"ankita":10,"anjali":20,"rani":30}
# m=[]
# l=[]
# for i in a:
#     m.append(i)
#     l.append(a[i])
# print(m)
# print(l)    

# l=["rani","bulbul","shweta"]
# dic={}
# for i in l:
#     dic.update({i:len(i)})
# print(dic)    

# l=[1,2,3,[3,4,2,[3,4],7]]
# i=0
# m=[]
# while i <len(l):
#     if type(l[i])==list:
#         j=0
#         while j<len(l[i]):
#             m.append(l[i][j])
#             j+=1
#     else:
#         m.append(l[i])        
#     i+=1 
# i=0
# n=[]
# while i<len(m):
#     if type(m[i])==list:
#         j=0
#         while j<len(m[i]):
#             n.append(m[i][j])
#             j+=1
#     else:
#         n.append(m[i])
#     i+=1
# print(n)    
# 
# l={"a":5,"b":[3,4],"c":[4,5]}
# m=[]
# h={}
# for t in l:
#     if type(l[t])==list:
#         m.append(l[t])
#         for i in range (len(m)):
#             sum=0
#             for j in range (len(m[i])):
#                 sum=sum+m[i][j]
#         h.update({t:sum})
#     else:
#         h.update({t:l[t]})
# print(h)

# l=[1,2,3,[3,4,2,[3,4],7]]
# i=0
# sum=0
# m=[]
# while i<len(l):
#     if type(l[i])==list:
#         j=0
#         while j<len(l[i]):
#             if type(l[i][j])==list:
#                 k=0
#                 while k<len(l[i][j]):
#                     m.append(l[i][j][k])
#                     k=k+1
#             else:
#                 m.append(l[i][j])

#             j=j+1
#     else:
#         m.append(l[i])
#     i=i+1  
# print(m)              
        




        




    
    
    
    






