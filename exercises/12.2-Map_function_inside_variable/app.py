names = ['Alice','Bob','Marry','Joe','Hilary','Stevia','Dylan']

prepended_names = []
def prepender(name):
    prepended_names = []
    #Your code go here:
    return "My name is: " + name

result = list(map(prepender, names))

print(result)



## ======== CODE FROM PREVIOUS EXERCISE ========= ## 
# def fahrenheit_values(Celsius_values):
# # the magic go here:
#     fahrenheit_values = []
#     # print(fahrenheit_values)
#     return (Celsius_values * 1.8) + 32

# result = list(map(fahrenheit_values, Celsius_values))
# print(result)
