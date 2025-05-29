from collections import UserList
# rotate elements by d places 
# brute approach with extra space O(d)
class Solution:
    def rotate(self, nums: UserList[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        temp = [] 
        n = len(nums)
        k = k % n
        for i in range(n-k,n):
            temp.append(nums[i])
        
        for i in range(n-k-1 , -1, -1):
            nums[i+k] = nums[i]

        for i in range(k):
            nums[i] = temp[i]
        return nums 

# optimal approach 
class Solution:
    def rotate(self, nums: UserList[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        n = len(nums)
        k %= n 
        nums.reverse()

        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])