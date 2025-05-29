from collections import UserList
# move the position of array element to the left by 1 
def leftrotate(arr):
    n = len(arr)
    temp = arr[0]
    for i in range(1,n):
        arr[i-1] = arr[i]
    arr[n-1] = temp
    return arr

# arr = list(map(int,input().split()))
# print(leftrotatebyd(arr))


# left rotate an array by d places 
# brute with sc = o(d) because of the temporary array
def leftrotatebyd(arr,d):
    n = len(arr)
    temp = []
    for i in range(0,d):
        temp.append(arr[i])

    for i in range(d,n):
        arr[i-d] = arr[i]

    for i in range(n-d,n):
        arr[i] = temp[i-(n-d)]
    return arr

arr = list(map(int,input().split()))
d = 3
print(leftrotatebyd(arr,d))


# left rotation optimal approach

def leftrotateoptimal(nums):
    k = 3
    n = len(nums)
    k %= n 


    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])

    nums.reverse()
    return nums
nums = [1,2,3,4,5,6,7]
print(leftrotateoptimal(nums))