import numpy as np

def ans(matrix, r, c):
    for i in range(0,r):
        if(matrix[i,0]+matrix[i,2]>matrix[i, 1] + matrix[i, 3]):
            print("perspolis")
        if (matrix[i, 0] + matrix[i, 2] < matrix[i, 1] + matrix[i, 3]):
            print("esteghlal")
        if (matrix[i, 0] + matrix[i, 2] == matrix[i, 1] + matrix[i, 3]):
            if(matrix[i, 1]>matrix[i, 2]):
                print("esteghlal")
            if (matrix[i, 2] > matrix[i, 1]):
                print("perspolis")
            if (matrix[i, 2] == matrix[i, 1]):
                print("penalty")



R = int(input())
C = 4

#print("Enter the entries in a single line (separated by space): ")

# User input of entries in a
# single line separated by space
#entries = list(map(int, input().split()))
matrix = [input().split() for i in range(R)] # if only row is given and the number of coloumn has to be decide by user
arr = np.array(matrix)
matrix2 = arr.astype(np.int)
# For printing the matrix
#matrix = np.array(entries).reshape(R, C)
#print(matrix2)

ans(matrix2, R, C)
