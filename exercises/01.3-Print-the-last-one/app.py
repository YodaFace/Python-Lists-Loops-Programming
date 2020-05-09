# import the random package here "import random"
import random

def generate_random_list():
    aux_list = []
    randonlength = random.randint(1, 100)

    for i in range(randonlength):
        aux_list.append(randonlength)
        i += i
    return aux_list
my_stupid_list = generate_random_list()

# Feel happy to write the code below this comment, good luck!:

## Create a variable named the_last_one
## Assign it the LAST element of my_stupid_list.

### the_last_one = my_stupid_list[-1]
length = len(my_stupid_list) 
the_last_one = my_stupid_list[length -1]
#variable = variable[function (variable) -1]

## Print the_last_one to the console.

print(the_last_one)

