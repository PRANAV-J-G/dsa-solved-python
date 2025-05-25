from collections import UserList
# move the position of array element to the left by 1 
def leftrotate(arr):
    n = len(arr)
    temp = arr[0]
    for i in range(1,n-1):
        arr[i-1] = arr[i]
        arr[n-1] = temp
    return arr

arr = list(map(int,input().split()))
print(leftrotate(arr))