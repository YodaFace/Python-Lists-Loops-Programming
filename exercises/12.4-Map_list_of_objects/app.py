import datetime


people = [
	{ "name": 'Joe', "birthDate": datetime.datetime(1986,10,24) },
	{ "name": 'Bob', "birthDate": datetime.datetime(1975,5,24) },
	{ "name": 'Erika', "birthDate": datetime.datetime(1989,6,12) },
	{ "name": 'Dylan', "birthDate": datetime.datetime(1999,12,14) },
	{ "name": 'Steve', "birthDate": datetime.datetime(2003,4,24) }
]


def calculateAge(birthDate):
    today = datetime.date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age


# THIS # 
def get_name(_dict):
    return _dict["name"]

name_list = list(map( get_name , people))

# IS THE SAME AS THIS 

name_list = list(map(lambda _dict:"Hello, my name is "+_dict["name"]+" and I am "+str(calculateAge(_dict["birthDate"]))+" years old", people))

# WHICH IS THE SAME # 

names_array = []

for _dict in people:
    names_array.append(_dict["name"])

print(name_list)


