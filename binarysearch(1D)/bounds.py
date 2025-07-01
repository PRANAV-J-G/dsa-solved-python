'''lower bound = lowest or smallest index that greater than or equal to arr[ind]'''

def lowerbound(nums,target):
    left,right = 0,len(nums)-1
    n = len(nums)
    ans = n 

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] >= target:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans

nums = [1,2,3,4,5,9,34,45] # here 34 is greater than or equal to 12 so the func returns index 5
target = 12
print(lowerbound(nums,target))


'''upper bound = lower or smallest index that is greater than arr[ind] ( not equal to)'''
def upperbound(nums,target):
    left,right = 0,len(nums)-1
    n = len(nums)
    ans = n 

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] > target:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans
