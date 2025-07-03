def brute(nums):
    return min(nums)

# O(n)


# slightly better approach
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        left , right = 0 ,len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
# binary search 
import sys
def optimal(nums):
    left , right = 0 , len(nums) - 1
    ans = sys.maxsize
    while left <= right:
        mid = (left + right) // 2   
        # even better time complexity 
        if nums[left] <= nums[right]:
            ans = min(ans,nums[left])

        if nums[left] <= nums[right]:
            ans = min(ans,nums[left])
        if nums[left] <= nums[mid]:
            ans = min(ans,nums[left])
            left = mid + 1
        else:
            ans = min(ans,nums[mid])
            right = mid - 1
    return ans
# even more optimized 
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        left , right = 0 ,len(nums) - 1
        ans = sys.maxsize

        while left <= right:
            mid = (left + right) // 2

            if nums[left] <= nums[right]:
                ans = min(ans,nums[left])
            if nums[left] <= nums[mid]:
                ans = min(ans,nums[left])
                left = mid + 1
            else:
                ans = min(ans,nums[mid])
                right = mid - 1
        return ans