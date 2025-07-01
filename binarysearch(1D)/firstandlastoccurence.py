# return index of the first and last occurence of the element 
# just do a linear search
from typing import List
def brute(nums: List[int], target: int) -> List[int]:
    first = -1
    last = -1

    for i in range(len(nums)):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    return first,last

nums = [5,7,7,8,8,10]
target = 8
print(brute(nums,target))


# using upper and lower bounds 

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lowerbound(nums,target):
            left , right = 0 , len(nums) - 1
            index = -1 
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
                if nums[mid] == target:
                    index = mid
            return index
        
        def upperbound(nums,target):
            left,right = 0,len(nums)-1
            index = -1

            while left <= right:
                mid = (left+right)//2

                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
                if nums[mid] == target:
                    index = mid
            return index

        return [lowerbound(nums,target),upperbound(nums,target)]              
    

# using binary search 
# use two binary searches to find the first and last occurence of the elements 
def binary(nums,target):
    def firstindex(nums,target):
        left , right = 0 ,len(nums) - 1
        ans = -1

        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                ans = mid 
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return ans
    
    def lastindex(nums,target):
        left , right = 0 , len(nums) - 1
        ans = - 1

        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                ans = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return ans
    return [firstindex(nums,target),lastindex(nums,target)]

nums = [2,8,8,8,8,8,9,11]
target = 8
print(binary(nums,target))



