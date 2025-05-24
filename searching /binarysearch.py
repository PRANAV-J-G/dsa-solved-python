def binarysearch(arr,target):
    left = 0 
    right = len(arr) - 1 

    while left <= right:
        mid = (left + right) // 2

        if target == arr[mid]:
            return mid 

        if target > arr[mid]:
            left = mid + 1 
        else:
            right = mid - 1 
    return -1 


arr = list(map(int,input().split()))
target = int(input('enter target:'))
print(binarysearch(arr,target))

