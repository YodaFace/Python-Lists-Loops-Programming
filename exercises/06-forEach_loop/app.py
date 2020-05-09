my_list = [3344,34334,454543,342534,4563456,3445,23455,234,262,2335,43323,4356,345,4545,452,345,434,36,345,4334,5454,345,4352,23,365,345,47,63,425,6578759,768,834,754,35,32,445,453456,56,7536867,3884526,4234,35353245,53244523,566785,7547,743,4324,523472634,26665,63432,54645,32,453625,7568,5669576,754,64356,542644,35,243,371,3251,351223,13231243,734,856,56,53,234342,56,545343]


for numb in my_list:
    #the magic go here:
    ##if numb is divisible by 14 
    if (numb % 14 == 0): 
    ## EXAMPLE if((number % 2) === 0)
        print(numb)
    

## FOUND ON A WEBSITE 

# for num in list:
# 	if( num%M==0 and num%N==0 ) :
# 		print num




# def findNoIsDivisibleOrNot(n, l =[]): 
  
#     # Checking if a number is divided 
#     # by every element or not 
#     for i in range(0, len(l)): 
#         if l[i]% n != 0: 
#             return 0
#     return 1
  
# # Driver code 
# l = [14, 12, 4, 18] 
# n = 2
# if findNoIsDivisibleOrNot(n, l) == 1: 
#     print "Yes"
# else: 
#     print "No"



# # Take a list of numbers
# my_list = [12, 65, 54, 39, 102, 339, 221,]

# # use anonymous function to filter
# result = list(filter(lambda x: (x % 13 == 0), my_list))

# # display the result
# print("Numbers divisible by 13 are",result)