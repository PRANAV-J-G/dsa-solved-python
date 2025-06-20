from collections import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue 

            a = nums[i]
        
            for j in range(i+1,n):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue 
                b = nums[j]

                left = j + 1 
                right = n - 1

                while left < right:

                    total = a + b + nums[left] + nums[right]

                    if total == target:
                        ans.append([a,b,nums[left],nums[right]])
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


        