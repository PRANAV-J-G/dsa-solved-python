from collections import UserList
class Solution:
    def maxFrequency(self, nums: UserList[int], k: int) -> int:
        nums.sort()  # n logn 

        left = right = total = res = 0

        while right < len(nums):
            total += nums[right]

            while nums[right]*(right - left + 1) > total + k:
                total -= nums[left]
                left += 1

            res = max(res,right - left + 1)
            right += 1
        return res