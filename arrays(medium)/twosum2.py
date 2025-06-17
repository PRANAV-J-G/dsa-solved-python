def twosum(nums,target):
    left = 0 
    right = len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return left+1,right-1
        if total < target:
            left += 1
        else:
            right -= 1 

nums = [2,7,11,15]
target = 9
print(twosum(nums,target))