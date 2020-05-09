
Celsius_values = [-2,34,56,-10]

def fahrenheit_values(Celsius_values):
# the magic go here:
    fahrenheit_values = []
    # print(fahrenheit_values)
    return (Celsius_values * 1.8) + 32

result = list(map(fahrenheit_values, Celsius_values))
print(result)

# print(fahrenheit_values())

### =========EXAMPLE FOUND ONLINE ===========###
# Python program to demonstrate working 
# of map. 
  
# Return double of n 
# def addition(n): 
#     return n + n 
  
# # We double all numbers using map() 
# numbers = (1, 2, 3, 4) 
# result = map(addition, numbers) 
# print(list(result)) 