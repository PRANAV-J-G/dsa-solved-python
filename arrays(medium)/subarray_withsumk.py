def brute(nums,k):
    count = 0
    for i in range(len(nums)):
        sum = 0
        for j in range(i,len(nums)):
            sum += nums[j]

            if sum == k:
                count += 1
    return count 
nums = [1,2,3,4,4,5,6,7,1,2]
k = 2
print(brute(nums,k))


# optimal solution 
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        hashmap = {0: 1}  # prefix_sum → frequency

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in hashmap:
                count += hashmap[prefix_sum - k]
            hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1

        return count