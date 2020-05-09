
tasks = [
	{ "label": 'Eat my lunch', "done": True },
	{ "label": 'Make the bed', "done": False },
	{ "label": 'Have some fun', "done": False },
	{ "label": 'Finish the replits', "done": False },
	{ "label": 'Replit the finishes', "done": True },
	{ "label": 'Ask for a raise', "done": False },
	{ "label": 'Read a book', "done": True },
	{ "label": 'Make a trip', "done": False }
]


#Your code go here:

# def filter_label(TrueOrFalse):
#     if TrueOrFalse in tasks == True: 
#         return TrueOrFalse

# print(type(tasks))
# print(type(tasks[0]))
# print(type(tasks[1]))
# print(type(tasks[3]))
# print(list(filter(filter_label, tasks)))


# print(list(filter(filter_label, tasks)))
print(list(filter(lambda tasks: tasks["done"] == True, tasks)))


# print(list(filter(lambda name: name[0] == "R", all_names)))



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
# print(list(filter(lambda name: name[0] == "R", all_names)))
