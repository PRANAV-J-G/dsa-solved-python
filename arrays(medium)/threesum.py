
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]: 
        ans = []
        
        nums.sort()

        for i in range(len(nums)): # also can use for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
        
            target = - nums[i]
            
            left = i + 1
            right = len(nums) -1
            
            while left < right:
                total = nums[left] + nums[right]
                
                if total == target:
                    ans.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1 
                
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1 
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1 
                        
                elif total < target:
                    left += 1 
                else:
                    right -= 1
        return ans 


    
                
            