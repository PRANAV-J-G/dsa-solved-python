# using two pointers (avoid mostly )
class Solution:
    def twoSum(self, nums, target):
        sorted_nums = sorted((num, i) for i, num in enumerate(nums))
        left, right = 0, len(nums) - 1

        while left < right:
            total = sorted_nums[left][0] + sorted_nums[right][0]
            if total == target:
                return [sorted_nums[left][1], sorted_nums[right][1]]
            elif total < target:
                left += 1
            else:
                right -= 1

s = Solution()
nums = [2, 7, 11, 5]
target = 9
print(s.twoSum(nums, target))  # Output: [0, 1]
