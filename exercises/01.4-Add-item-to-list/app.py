#Remember import random function here:

import random

my_list = [4,5,734,43,45]

#The magic is here:

#def random - Defines a function "random"
#Calling without "def"
## random_number = random.random() 

## random()
# print (random_number) - for testing

#-------------------------------------------------------
### the_last_one = my_stupid_list[-1]
        #length = len(my_stupid_list) 
        #the_last_one = my_stupid_list[length -1]
#variable = variable[function (variable) -1]

## Print the_last_one to the console.

#print(the_last_one)
#-------------------------------------------------------

i = range(len(my_list))

for i in range(10):
    random_number = random.randint(0,1000) 
    my_list.append(random_number)
    
    #if my_list(len(my_list))
    #my_list.append(random_number)


print (my_list)