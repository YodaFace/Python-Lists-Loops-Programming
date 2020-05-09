
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
# def only_rs(names):
#     names_with_rs = []  
#     if "R" in names:

#     #if "R" in names and "None" not in names:
#         return names
#     # return names if "R" in names

# # only_rs()

# resulting_names = list(filter(only_rs, all_names))

# #resulting_names = list(map(only_rs, all_names))

# print(resulting_names)



## BEST WAY ## 
# def filter_name(name):
#     return name[0] == "R" 

## SECOND BEST WAY ## 
# def filter_name(name):
#     if name[0] == "R":
#         return True

# resulting_names = filter(filter_name, all_names)
# print(list(resulting_names))


## LAMBDA WAY (Arguably the best way) ## 
print(list(filter(lambda name: name[0] == "R", all_names)))






# Your code go here:
# def only_rs(names):
#     #names_with_rs = []  
#     if "R" in names:
#         return names
#     else:
#         return






### OTHER STUFF THAT WAS TRIED ###

    # names_with_rs.append(names)
    # if "" in names: 
    #      names_with_rs.remove(names)
    #names_with_rs = list(filter(None, names_with_rs))
    # print(names_with_rs)
    # print(type(names_with_rs))