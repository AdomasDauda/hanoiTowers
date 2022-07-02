from copy import copy

plane = [[0,1,0],
         [0,2,0],
         [0,3,0],
         ]

def transpose(y):
    m = len(y)
    n = len(y[0])
    x = [0] * n
    for b in range (n):
        x[b] = [0] * m

    for i in range(len(y)):
        for j in range(len(y[0])):
           x[j][i] = y[i][j]
    return x


def check(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])-1):
            if mat[i][j] > mat[i][j+1]:
                return False
    return True


def areSame(A,B):
    m = len(A)
    n = len(A[0])

    for i in range(m):
        for j in range(n):
            if (A[i][j] != B[i][j]):
                return False
    return True


def heights(mat): # the matrix  has to be transposed
    columnHeights = []
    for i in range(len(mat)):
        k = 0
        for p in mat[i]:

            if p != 0: # the top number will be there only if its the start or the finish
                height = len(mat[i]) - k # when its the first row it means the height is 3
                columnHeights.append(height)
                break

            if p == 0 and k == len(mat[i])-1:
                columnHeights.append(0)

            if p == 0:
                k += 1
                
    return columnHeights




matx = transpose(plane)




prevStep = copy(matx)
while True:
    #main code

    if areSame(transpose(matx), plane) == False and check(matx) == True: # checks if it is not the same as at the start and if it is in order
        break


    columnHeights = heights(matx)
    

    if check(matx) == False:
        matx = prevStep