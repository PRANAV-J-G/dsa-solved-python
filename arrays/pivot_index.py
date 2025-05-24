from collections import UserList 
class Solution:
    def pivotIndex(self, nums: UserList[int]) -> int:
        total_sums = sum(nums)
        left_sum = 0 

        for i in range(len(nums)):
            # since right_sum = total_sums - left_sum - nums[i]
            if left_sum == total_sums - left_sum - nums[i]:
                return i 
            left_sum += nums[i]

        return -1 

s = Solution()
nums = list(map(int,input().split()))
print(s.pivotIndex(nums))