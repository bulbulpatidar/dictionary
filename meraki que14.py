            
dic={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
a=[]
c={}
for i in dic:
    a.append(dic[i])   
for j in range(len(a)):
    for k in range(len(a)-1):
        if a[k]>a[k+1]:
            t=a[k]
            a[k]=a[k+1]
            a[k+1]=t        
for m in range(len(a)):
      for l in dic:
          if dic[l]==a[m]:
              c.update({l:(dic[l])})
print(c)              

# dic={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# a=[]
# c={}
# for i in dic:
#     a.append(dic[i])
# for j in range(len(a)):
#     for k in range(len(a)-1):
#         if a[k]<a[k+1]:
#             t=a[k]
#             a[k]=a[k+1]
#             a[k+1]=t
# print(a)
# for m in range(len(a)):
#     for l in dic:
#         if dic[l]==a[m]:
#             c.update({l:(dic[l])})
# print(c)            
