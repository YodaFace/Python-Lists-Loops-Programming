chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
#1. Declare an empty list. 
    chunky_combo = []
# 2. Loop the two list. 
    for names in chunk_one:
# 3. Concatenate the result in an empty lists. 
        chunky_combo.append(names)
    for names in chunk_two:
        chunky_combo.append(names)
# 4. Print the variable with two list
    return chunky_combo
    
print(merge_list(chunk_one, chunk_two))



# def deletePerson(person_name):
#     #Your code go here:
#     new_people = []
#     for person in people:
#         people2 = people
#         if person != person_name:   
#             new_people.append(person)
#             #print(person_name)
#         #people.insert(person_name)
#         #print(people)
#         #print(person_name) 
#     return new_people