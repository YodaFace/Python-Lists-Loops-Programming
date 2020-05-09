theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:


def isTrueOrFalse(ones_and_zeros):
    if ones_and_zeros == 1:
        return "wiki"
    else:
        return "woko"


the_bools_words = list(map(isTrueOrFalse, theBools))
print(the_bools_words)

# print(the_bools_words)


## ======== CODE FROM PREVIOUS EXERCISE ========= ## 
# def increment_by_one(the_number):
#     return the_number * 3

# new_list = map(increment_by_one, myNumbers)
# result = list(map(increment_by_one, myNumbers))  ## THIS WAS NOT NECESSARY IN THE OTHER ONE


# print(result)
