# simpler solution in n runtime 
from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) ==  1:
            return nums[0]
        for i in range(0,len(nums)-1,2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]



# another brute force 
def single(nums):
    if len(nums) == 1:
        return nums[0]
    for i in range(len(nums)):
        if i == 0:
            if nums[i] != nums[i+1]: return nums[i]
        elif i == len(nums) - 1:
            if nums[i] != nums[i-1]: return nums[i]
        else:
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                return nums[i]
        
# optimal solution 

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        # check for the left pointer
        if nums[0] != nums[1]:
            return nums[0]
        # check for the right pointer
        if nums[n-1] != nums[n-2]:
            return nums[n-1]
        
        left , right  = 1 , n - 2 
        while left <= right:
            mid = (left+right)//2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            # eliminate left half 
            elif (mid % 2 == 1) and nums[mid - 1] == nums[mid] or (mid % 2 == 0) and nums[mid] == nums[mid + 1]:
                left = mid + 1
            # eliminate right half 
            else:
                right = mid - 1
        return - 1


# optimal solution
def optimal(nums):
    return arr 
    