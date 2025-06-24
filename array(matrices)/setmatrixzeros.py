# if an array is zero set it's entire row and column as zero 
# O(n*m)*(n+m)+(n*m)
def brute(matrix):
    
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                # changes the element of the row except 0 to -1
                for col in range(m):
                    if matrix[i][col] != 0:
                        matrix[i][col] = 'X'
                # changes the element of the cols except 0 to - 1
                for row in range(n):
                    if matrix[row][j] != 0:
                        matrix[row][j] = "X"
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'X':
                matrix[i][j] = 0



# better solution 
#tc = O 2*(n*m)
def better(matrix):
        n = len(matrix)
        m = len(matrix[0])
        # create 2 extra arrays , to store the cols and rows containing zeros 
        row = [0] * n
        col = [0] * m 

        for i in range(n):
            for j in range(m):
                 if matrix[i][j] == 0:
                    row[i] = 1
                    col [j] = 1
        for i in range(n):
            for j in range(m):
                if row[i] == 1 or col[j] == 1:
                    matrix[i][j] = 0

# optimal solution 
# tc 2*(m*n) with no extra space
def optimal(matrix):
    col0 = 1
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                # mark the ith row as 0
                matrix[i][0] = 0

                # mark the jth col as 0
                if j!= 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0
    
    for i in range(1,n):
        for j in range(1,m):
            if matrix[i][j] != 0:
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
    if matrix[0][0] == 0:
        for j in range(m):
            matrix[0][j] = 0
    
    if col0 == 0:
        for i in range(n):
            matrix[i][0] = 0
        

