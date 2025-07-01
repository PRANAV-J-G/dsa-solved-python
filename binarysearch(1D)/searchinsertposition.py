def search(nums,target):
    left , right = 0 ,len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left

nums = [1,2,4,7]
target = 2
print(search(nums,target))


# or just find the lower bound 
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