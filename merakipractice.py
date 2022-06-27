# city_population = {"NewYorkCity":8550405,"LosAngeles":3971883, "Toronto":2731571, "Chicago":272054,"Houston":2296224, 
# "Montreal":1704694, 
# "Calgary":1239220, 
# "Vancouver":631486, 
# "Boston":667137
# }

# print(city_population["NewYorkCity"])

# Dict = {
# 'ball' : 'green',
# 'Ball': 'red'}
# print(Dict['ball'])
# print(Dict['Ball'])
# # print(Dict['bat'])

# student=dict(name= "Ravina",age= 20)
# print(student)

# Dic= {
#  1: 'NAVGURUKUL',
#  2: 'IN',  
#  3:{'A' : 'WELCOME','B' : 'To', 
# 'C' : 'DHARAMSALA'}}
# print(Dic)

# person={'name':'jack','age':20,'gender':'male',4:'organisation'}

# result = person['age'] 
# x = person.get("gender")
# print(person[4])
# print(x)
# print(result)

# person={'name':'jack','age':20,'gender':'male',4:{'organisation':'navgurukul','place':'dharamsa'}}
# print(person['gender'])

# print(person[4])

# result = person[4]['place']

# print(result)

# dic= {'Name': 'RAM', 'Age': 17,}
# dic['ORGANIZATION'] = "NAV GURUKUL"

# dic['place'] = 'dharamsala'
# dic['education']='graduation'

# print(dic)


# dic= {'Name': 'RAM','Age': 17,}
# dic['student']={'id':22, 'place':'dharamsala'}
# print(dic)

# car ={"brand":  "ford","model":  "mustang","year":  1964}
# if "model" in car:
#       print("Yes, 'model' is one of the keys in the car dictionary.")
# else:
#     print("No, 'model' key dictionary mai nahi hai.")


# person= {'1': 'RAM', '2': 17,}
# person[3] = 'male'
# print(person)


# details={'Name': 'RAM','Age': 17, 'student': {'id': 22,'place': 'dharamsala'}} 
# details['student']['id']=35
# print(details)


# classes ={"room1":  "6th","room2":  "7th","room3":  "8th"}
# mydict=classes.copy()
# print(mydict)

# CAR_DETAILS={"brand": "Ford","model": "jason","year": 1964}
# CAR_DETAILS.pop("model")
# print(CAR_DETAILS)


# person={'name':'jack','id':22,'place':'dharamsala'}
# person.popitem()
# print(person)

# person={'name':'jack','id':22,'place':'dharamsala'}
# del person('place')
# print(person)

# states_capitals = {'Gujarat' : 'Gandhinagar','Maharashtra' : 'Mumbai','Rajasthan' : 'Jaipur','Bihar' : 'Patna'}
# for state in states_capitals:
#   print(state,states_capitals[state])

# states_capitals = {'Gujarat' : 'Gandhinagar','Maharashtra' : 'Mumbai','Rajasthan' : 'Jaipur','Bihar' : 'Patna'}
# for state in states_capitals:
#    print(states_capitals[state])

# details ={"name":  "Bijender","age":  17,"class":  "10th"}
# for x in details.values():
#     print(x)

# movie ={"name":  "Puli","hero":  "Vijay","rating":  7.5}
# for x,y in movie.items():
#     print(x,y)

# meal ={"monday":  "Chole chawal","sunday":  "Fried rice","wednesday":  "dosa"}
# print(len(meal))

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# # x = thisdict["model"]
# x = thisdict.get("model")
# print(x)

# car = {"brand": "Ford","model": "Mustang","year": 1964}
# x = car.keys()
# print(x) #before the change
# car["color"] = "white"
# print(x) #after the change 

# car = {"brand": "Ford","model": "Mustang","year": 1964}
# x = car.values()
# print(x)
# 
# car = {"brand": "Ford","model": "Mustang","year": 1964}
# x = car.items()
# print(x) #before the change
# car["year"] = 2020
# print(x) #after the change 
# 
# thisdict =	{"brand": "Ford","model": "Mustang","year": 1964}
# thisdict["year"] = 2018 
# print(thisdict)

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020}) 
# print(thisdict)

# thisdict =	{"brand": "Ford","model": "Mustang","year": 1964}
# thisdict.pop("brand")
# print(thisdict) 

# thisdict =	{"brand": "Ford","model": "Mustang","year": 1964}
# thisdict.popitem()
# print(thisdict) 

# thisdict =	{"brand": "Ford","model": "Mustang","year": 1964}
# del thisdict["model"]
# print(thisdict) 


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict =thisdict.copy()
# print(mydict) 


