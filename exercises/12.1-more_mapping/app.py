myNumbers = [23,234,345,4356234,243,43,56,2]

#Your code go here:

def increment_by_one(the_number):
    # new_list = []
    # new_list.append(the_numbers * 3)
    # print(new_list)
    # new_list.append(the_numbers) * 3
    return the_number * 3
    # return new_list

new_list = map(increment_by_one, myNumbers)
result = list(map(increment_by_one, myNumbers))

#print(new_list)
print(result)

# increment_by_one(myNumbers)

## ======== CODE FROM PREVIOUS EXERCISE ========= ## 
# def fahrenheit_values(Celsius_values):
# # the magic go here:
#     fahrenheit_values = []
#     # print(fahrenheit_values)
#     return (Celsius_values * 1.8) + 32

# result = list(map(fahrenheit_values, Celsius_values))
# print(result)