# brute solution 
def brute(matrix):
    n = len(matrix)
    m = len(matrix[0])  
    ans = [[0 for i in range(n)] for j in range(m)]
    for i in range(n):
        for j in range(m):
            matrix[j][n-i-1] = matrix[i][j]
    return ans

def optimal(matrix):
    n = len(matrix)
    m = len(matrix[0])
    # traverse only the top right half of the matrix 
    # ie the elements above the diagonal 
    for i in range(n-1):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

    for row in matrix:
        row.reverse()