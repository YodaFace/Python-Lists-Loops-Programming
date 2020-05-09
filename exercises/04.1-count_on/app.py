
my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]


#your code go here:

hello = [ ]


for i in my_list:
    if type(i) == list or type(i) == dict:
        hello.append(i)
    #hello = type(i)
    #hello.append(i)
    #print(i)
    #print(hello)
    #print(hello)



# Alternatively, you can use create a new list, and append to it:

#     out = []
#     for object in L:
#         if condition:
#             out.append(object)


# FROM LAST EXCERCISE 
# for i in mix:
#     print (type(i))

# FOUND ON INTERNET 
# dicts = {}
# keys = range(4)
# values = ["Hi", "I", "am", "John"]
# for i in keys:
#         dicts[i] = values[i]
# print(dicts)


#   list = []          ## Start as the empty list
#   list.append('a')   ## Use append() to add elements
#   list.append('b')

# to insert one list in another 
# for i in range(len(insert_list)): 
#     test_list.insert(i + pos, insert_list[i]) 
  

# Alternatively, you can use create a new list, and append to it:

#     out = []
#     for object in L:
#         if condition:
#             out.append(object)