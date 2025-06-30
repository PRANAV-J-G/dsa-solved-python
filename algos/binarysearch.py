def binarysearch(nums,target):
    left , right = 0 ,len(nums)-1
    while left <= right:
        mid = (left+right)//2

        if target == nums[mid]:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left 

nums = [1,2,3,4,6,78,98,101]
target = 78
print(binarysearch(nums,target))
# tc  = O(logn)

# using recursion 

def recursivebinarysearch(nums,low,high,target):
    nums.sort()
    if low > high:
        return - 1
    mid = (low + high) // 2 

    if nums[mid] == target:
        return mid
    elif target > nums[mid]:
        return recursivebinarysearch(nums,mid+1,high,target)
    else:
        return recursivebinarysearch(nums,low,mid-1,target)
    
nums = [1,2,3,4,6,78,98,101]
target = 78
low = 0 
high = len(nums) - 1
print(recursivebinarysearch(nums,low,high,target))

#overflow case 
'''
when the high pointer is in a sys.max int and the calculation of mid becomes 2*maxsize that causes the value to overflow
use long instead 
or use 
mid = low + (high - low) // 2
'''