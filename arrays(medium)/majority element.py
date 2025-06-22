# find element occuring more than n // 2 times

def brute(nums):
    for i in range(len(nums)):
        count = 0 
        n = len(nums)
        for j in range(len(nums)):
            if nums[j] == nums[i]:
                count += 1
            
        if count > n // 2:
            return nums[i]
        
# better solution using hashing
from collections import defaultdict
from typing  import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)

        for i in range(len(nums)):
            hashmap[nums[i]] += 1
        
        for key,value in hashmap.items():
            if value > len(nums) // 2:
                return key  
        return None

# optimal solution 
# moore voting algorithm
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0 
        element = 0 

        for num in nums:
            if count == 0:
                element = num
            if num == element:
                count += 1
            else:
                count -= 1
        return element