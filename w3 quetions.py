# d={0: 10, 1: 20}
# d[2]=30
# print(d)

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# l={}
# for i in (dic1,dic2,dic3):
#     l.update(i)
# print(l) 


# keys = ['red', 'green', 'blue']
# values = ['#FF0000','#008000', '#0000FF']
# d1 = {}

# for k,v in zip(keys,values):
#      d1[k] = v
# print(d1)     

# dic=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# d={}
# for i in dic:
#     if i["item"] not in d:
#         d[i["item"]]=i["amount"]
#     else:
#         d[i["item"]]+=i["amount"]
# print(d)           
        

# sample = {'Math':81, 'Physics':83, 'Chemistry':87}

# sort_sample = sorted(sample.items())
# print(sort_sample)

# l1=['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
# l2=[1, 2, 2, 3]
# d={}
# for k,v in zip(l1,l2):
#     d[k] = {v}
# print(d)

# l1=['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
# l2=[1, 2, 2, 3]
# l={}
# for i in range(len(l1)):
#     l.update({l1[i]:{l2[i]}})
# print(l)    


# a=[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# b=[]
# for i in a:
#      b.append(i['Math'])
# print(b)