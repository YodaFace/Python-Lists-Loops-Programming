my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

#Your code here:

auxiliar = 0
for i in my_list:
    auxiliar += i 

print(auxiliar / len(my_list))


# https://www.geeksforgeeks.org/find-average-list-python/

# def Average(lst): 
#     return sum(lst) / len(lst) 

# # Driver Code 
# lst = [15, 9, 55, 41, 35, 20, 62, 49] 
# average = Average(lst) 
  
# # Printing average of the list 
# print("Average of the list =", round(average, 2))


# https://www.educative.io/edpresso/how-to-take-the-average-of-a-list-in-python
# Essentially the same way of doing it 
# def Average(l): 
#     avg = sum(l) / len(l) 
#     return avg
  
# my_list = [2,4,6,8,10] 
# average = Average(my_list) 
  
# print("Average of my_list is", average)