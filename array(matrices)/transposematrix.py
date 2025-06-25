def transpose(matrix):

    n = len(matrix)
    m = len(matrix[0])
    # traverse only the top right half of the matrix 
    # ie the elements above the diagonal 
    for i in range(n-1):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

    
