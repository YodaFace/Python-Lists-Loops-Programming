list_of_numbers = [4,	80,	85,	59,	37,25,	5,	64,	66,	81,20,	64,	41,	22,	76,76,	55,	96,	2,	68]


#Your code here:
def merge_two_list(list_of_numbers):  
    odd = []
    even = []
    for numb in list_of_numbers:
        if numb % 2 != 0:
            odd.append(numb)
        else:
            even.append(numb)
    merge_two_list = odd+even
    return merge_two_list

print(merge_two_list(list_of_numbers))

