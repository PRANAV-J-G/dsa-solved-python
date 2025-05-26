def linearsearch(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i
    return -1 

arr = [ 1,2,3,4,5,6,7]
target = 7
print(linearsearch(arr))
# just iterate to find the element 
