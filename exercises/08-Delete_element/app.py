people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:

def deletePerson(person_name):
    #Your code go here:
    new_people = []
    for person in people:
        people2 = people
        if person != person_name:   
            new_people.append(person)
            #print(person_name)
        #people.insert(person_name)
        #print(people)
        #print(person_name) 
    return new_people


print(deletePerson("daniella"))
# deletePerson("daniella")
# print(people2)
print(deletePerson("juan"))
# deletePerson("juan")
# print(people2)
print(deletePerson("emilio"))
# deletePerson("emilio")
# print(people2)
