
arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:

#STEP 1 "Create a function called sumOdds
def sumOdds():
    auxiliar = 0 
    for i in arr:
        if i % 2 != 0:
            auxiliar = auxiliar + i 
    return auxiliar
    #STEP 2 "that sums all the odd numbers in the "arr" variable.""

print(sumOdds())
