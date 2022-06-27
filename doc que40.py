d1=['S001', 'S002', 'S003', 'S004']
d2=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
d3=[85, 98, 89, 92]
l={}
for i in range(len(d1)):
    l.update({d1[i]:{(d2[i]):d3[i]}})
print([l])  

