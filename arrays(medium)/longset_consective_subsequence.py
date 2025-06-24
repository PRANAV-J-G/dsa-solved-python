# brute force solution 
from typing import List
def longestConsecutive(self, nums: List[int]) -> int:
    max_len = 0
    
    for num in nums:
        current = num
        count = 1

        # Check if next consecutive numbers exist
        while current + 1 in nums:
            current += 1
            count += 1

        max_len = max(max_len, count)

    return max_len


#  better solution 
# sorting always takes nlogn
def better(nums):
    nums.sort()
    longest = 1
    count_curr = 0 
    last_smaller = float('-inf')

    for i in range(len(nums)):
        if nums[i-1] == last_smaller:
            count_curr += 1
            last_smaller = nums[i]
        elif nums[i] != last_smaller:
            count_curr = 1
            last_smaller = nums[i]
        longest = max(longest,count_curr)
    return longest       


# optimal solution 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0

        for num in num_set:
            # Start counting only if it's the beginning of a sequence
            if num - 1 not in num_set:
                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                max_length = max(max_length, length)

        return max_length