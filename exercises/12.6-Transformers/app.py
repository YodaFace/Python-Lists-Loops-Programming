
incomingAJAXData = [
	{ "name": 'Mario', "lastName": 'Montes' },
	{ "name": 'Joe', "lastName": 'Biden' },
	{ "name": 'Bill', "lastName": 'Clon' },
	{ "name": 'Hilary', "lastName": 'Mccafee' },
	{ "name": 'Bobby', "lastName": 'Mc birth' }
]

#Your code go here:

def my_var(full_name):
    name = full_name["name"]
    last_name = full_name ["lastName"]
    return name + " " + last_name


transformedData = list(map(my_var, incomingAJAXData))
print(transformedData)



## FROM PREVIOUS EXERCISE ## 
# the_bools_words = list(map(isTrueOrFalse, theBools))
# print(the_bools_words)

# name_list = list(map(lambda person:  person["name"] , people))
# print(name_list)