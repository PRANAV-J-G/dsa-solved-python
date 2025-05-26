class Solution:

# move zeroes to the end in the brute force approach 
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonzero = 0 
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[nonzero] = nums[i]
                nonzero += 1
        for i in range(nonzero , len(nums)):
            nums[i] = 0 

#optimal approach with no extra space and linear time 

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = -1 
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                j = i
                break
        if j == -1: return nums
        for i in range(j+1,n):
            if nums[i] != 0:
                nums[j],nums[i] = nums[i],nums[j]
                j += 1