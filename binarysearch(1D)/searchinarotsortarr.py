# search in a rotated and sorted array ( unique elements) 
# linear search is the brute force 
# ( intuition - atleast one half of the rotated array is sorted from the middle pointer)
# identify the sorted half first
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left , right = 0 , len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid 
            # check left half sorted 
            if nums[left] <= nums[mid]:
                if nums[left] <= target and target <= nums[mid]:
                    right = mid - 1 
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1  
        return -1
    

# search in a rotated array with duplicate elements 
# the first approach fails if the left , right and the mid pointed values are same 
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left , right = 0 , len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            
            if nums[mid] == nums[left] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1  
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
