my_list = [ 1, 0, 0, 0, 1, 0, 0, 0, 1, 1 ]

def my_function(numbers):
    new_list = []
    for numb in numbers:
    #The magic go here:
        if numb == 1:
            new_list.append(numb)
            #print(new_list)
        if numb == 0:
            new_list.append("Yahoo")
            #print("Yahoo")

    return new_list
print(my_function(my_list))


## FOUND ON WEBSITE ## 
# # Create a list of numbers (our shopping cart)
# cart = [3, 4, 12, 17, 19, 21, 23, 26, 30]
# # Pass items to the cashier
# cashier = []
# for item in cart:
#     cashier.append(item)
# print(cashier)
# # The output is the same as the cart
# Output: [3, 4, 12, 17, 19, 21, 23, 26, 30]
