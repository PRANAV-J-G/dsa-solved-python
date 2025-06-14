def sortingapproach(nums):
    n = len(nums)
    nums.sort()
    for j in range(n-1):
        if nums[j] == nums[j+1]:
            return True
    return False

nums = [1,2,3,4,1]
print(sortingapproach(nums))


## Hashset 

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
# Hashmap 

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = {}

        for num in nums:
            if num in seen and seen[num] >= 1:
                return True 
            seen[num] = seen.get(num,0) + 1
        return False
