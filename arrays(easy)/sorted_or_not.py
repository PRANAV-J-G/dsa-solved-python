def checksort(arr): #TC 0(N)
    for i in range(len(arr)-1): # -1 to avoid out of index errors
        if arr[i] > arr[i+1]:
            return False
    return True

arr = list(map(int,input().split()))
print(checksort(arr))

#2 second option  (same time complexity)
def check(arr):
    for i in range(1,len(arr)): #no need to check for the first element 
        if arr[i] >= arr[i-1]:
            pass
        else:
            return False
    return True
arr = list(map(int,input().split()))
print(check(arr))