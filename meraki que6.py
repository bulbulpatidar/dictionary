dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
c={}
for i in dic:
    # if i not in c:
        c.update({i:(dic[i])})
print(c)  
