# brute force approach 
'''
1) Generate all the permutations
2) Linear search through the permutations to find the index of the desired permutation
3)Return the next permutation if there are none return the sorted array
'''

# better solution only applies to c++ using stl 

# optimal solution 
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1
        n = len(nums)
        for i in range(n-2,-1,-1): # traverse in reverse to find the element that is greater than  current permutation
            if nums[i+1] > nums[i]:
                index = i 
                break
        
        if index == -1:
            return nums.sort()

        for i in range(n-1,index,-1): # finding the closest greater number
            if nums[i] > nums[index]:
                nums[i],nums[index] = nums[index],nums[i]
                break
        
        nums[index+1:] = nums[index+1:][::-1] # reversing the rest to get the next perm

