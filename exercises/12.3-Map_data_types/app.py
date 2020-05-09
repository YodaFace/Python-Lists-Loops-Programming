list_Strings = ['1','5','45','34','343','34',6556,323]


def type_list(items):
        return type(items)

new_list = list(map(type_list, list_Strings))
print(new_list)



## ======== CODE FROM PREVIOUS EXERCISE ========= ## 
# def fahrenheit_values(Celsius_values):
# # the magic go here:
#     fahrenheit_values = []
#     # print(fahrenheit_values)
#     return (Celsius_values * 1.8) + 32

# result = list(map(fahrenheit_values, Celsius_values))
# print(result)