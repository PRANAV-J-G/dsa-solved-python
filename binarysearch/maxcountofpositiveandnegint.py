# optimal solution 
from typing import List
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0 
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2 
            if nums[mid] < 0:
                left = mid + 1 
            else:
                right = mid - 1
        negative_count = right + 1

        left , right = 0 , n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > 0:
                right = mid - 1 
            else:
                left = mid + 1
        positive_count = n - left 
    
        return max(positive_count,negative_count)
    

# better solution 
def better(nums):
    negative = 0 
    positive = 0 

    for i in range(len(nums)):
        if nums[i] == 0:
            continue 
        if nums[i] > 0:
            positive += 1
        else:
            negative += 1
    return max(negative,positive)
