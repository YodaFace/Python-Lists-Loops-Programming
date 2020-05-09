
names = ['Liam','Emma','Noah','Olivia','William','Ava','James','Isabella','Logan','Sophia',
'Benjamin','Mia','Mason','Charlotte','Elijah','Amelia','Oliver','Evelyn','Jacob','Abigail',
'Lucas','Harper','Michael','Emily','Alexander','Elizabeth','Ethan','Avery','Daniel','Sofia',
'Matthew','Ella','Aiden','Madison','Henry','Scarlett','Joseph','Victoria','Jackson','Aria',
'Samuel','Grace','Sebastian','Chloe','David','Camila','Carter','Penelope','Wyatt','Riley']

#Your code go here:

def am_present(name):
        if "am" in name:
            return name
        # result = quote.rfind('am')
        # return name

print(list(filter(am_present, names)))

# print(list(filter(filter_label, tasks)))


## BEST WAY ## 
# def filter_name(name):
#     return name[0] == "R" 

# def filter_function(items):
#     return items > 10