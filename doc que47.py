
l={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
for i ,j in l.items():
    for i in range(len(j)):
        j.clear()
print(l)        