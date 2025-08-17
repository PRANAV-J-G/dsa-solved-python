# brute force approach is definitely the nested loop structure with n**2 time complexity

def optimal(mat):
    rows = len(mat)
    cols = len(mat[0]) 

    low = 0 
    high = cols - 1

    def maxelement(mat,rows,cols,mid):
        index = -1
        maxvalue = -1
        for i in range(rows):
            if mat[i][mid] > maxvalue:
                maxvalue = mat[i][mid]
                index = i 
        return index
    while low <= high:
        mid = (low + high) // 2
        row = maxelement(mat,rows,cols,mid)

        left = -1 if mid-1 <= 0 else mat[row][mid-1]
        right = -1 if mid+1 >= cols else mat[row][mid+1] 

        if mat[row][mid] > left and mat[row][mid] > right:
            return row,mid
        elif mat[row][mid] < left:
            high = mid - 1
        else:
            low = mid + 1
    return -1

    