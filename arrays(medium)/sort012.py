# brute force is any of the sorting algorithm 

def better(nums):
    count0 = 0
    count1 = 0 
    count2 = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            count0 += 1
        elif nums[i] == 1:
            count1 += 1
        else:
            count2 += 1
    
    for i in range(count0):
        nums[i] = 0
    
    for j in range(count0,count1 + count0):
        nums[j] = 1
    
    for k in range(count1+count0,len(nums)):
        nums[k] = 2
    
    return nums

nums = [0,1,1,0,2,2,0,1,1,2]
print(better(nums))  #tc = O(2n)


# optimal solution 
# dutch national flag algorithm solution 
'''
visualize 0 to low - 1 == 0
low to mid-1 == 1
mid+1 to high == unsorted array (actual array to sorted)
high+1 to n-1 == 2'''

# tc  = O(n)  sc = O(1)
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left , mid  = 0 , 0
        high = len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:
                nums[mid],nums[left] = nums[left],nums[mid]
                mid += 1
                left += 1
            elif nums[mid] == 1:
                 mid += 1
            else:
                nums[mid],nums[high] = nums[high],nums[mid]
                high -= 1



