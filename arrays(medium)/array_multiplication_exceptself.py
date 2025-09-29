# using prefix and postfix sum
from typing import List     
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)

        prefix = 1
        
        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i]
        
        postfix = 1 

        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix 
            postfix *= nums[i]
        return res        

# brute force with n2 tc 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j:
                    continue    
                prod *= nums[j]
            
            res[i] = prod
        return res
    
# using division 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt +=  1
        if zero_cnt > 1: return [0] * len(nums)

        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_cnt: res[i] = 0 if c else prod
            else: res[i] = prod // c
        return res