class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        result = 0 
        maximum = 0 
        for num in nums:
            if num == 1:
                result += 1 
                maximum = max(result,maximum)
            else:
                result = 0
        return maximum
