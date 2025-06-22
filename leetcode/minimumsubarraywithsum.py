# returning the length of the minimum subarray with sum = k 
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0 
        length = float('inf')      
        curr_sum = 0
        for right in range(len(nums)):

            curr_sum += nums[right]

            while curr_sum >= target:
                length = min(length,right-left+1)
                curr_sum -= nums[left]
                left += 1
        return 0 if length == float('inf') else length
    
