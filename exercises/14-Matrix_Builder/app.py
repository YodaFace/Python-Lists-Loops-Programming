import random

#Create the function below:

def matrixBuilder(i):
    numb_of_matrix = i
    # matrix = []
    matrix = [1] * numb_of_matrix
    for i in range(numb_of_matrix):
        matrix[i] = [1] * numb_of_matrix 
        # tried this : matrix[i].append(",\n")
        # tried this : matrix.append(",\n")
    print(matrix)


matrixBuilder(5)


### EXAMPLE FOUND ON INTERNET ### 
# https://snakify.org/en/lessons/two_dimensional_lists_arrays/ # 
# n = 3
# m = 4
# a = [0] * n
# for i in range(n):
#     a[i] = [0] * m


# print(a)




### TRYING  TO CODE ##### 
# def matrixBuilder(i):
#     matrix = []
#     matrixes = []
#     for i in range(i):
#         matrix.append([1] * (i+1))
#         print(matrix)
#         print("Plus One")
#         print(matrix)
#     print("Out of For Loop")
#         if length of len(matrixes) != i:
#             matrixes.append(matrix[-1])
#     print(matrix)
#     print(matrixes)

# matrixBuilder(5)

### PLAYING WITH CODE ##### 
# n1 = [0 for i in range(20)]
# n2 = [0] * 15

# print(n1)
# print(n2)

# n1[0:11] = [10] * 10

# print(n1)


# a = [1,2,3] 
# b = list([1,2,3])

# print(a == b)

# print(a)
# print(b)
