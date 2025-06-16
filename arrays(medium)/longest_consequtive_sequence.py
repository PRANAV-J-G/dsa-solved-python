# brute force 
from collections import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for num in nums:
            streak, curr = 0, num
            while curr in store:
                streak += 1
                curr += 1
            res = max(res, streak)
        return res
    
# using hashset
# O(n)
def hashset(nums):
    numset = set(nums)
    longest = 0 

    for num in nums:
        if num - 1 not in numset:
            length = 1 

            while (num + length) in numset:
                length += 1
            longest = max(length,longest)
    return longest

# using hashmap 
# O(n)
from collections import defaultdict
def hashmap(nums):
    mp = defaultdict(int)
    res =  0 

    for num in nums:
        if not mp[num]:
            mp[num] = mp[num - 1] + mp[num + 1] + 1
            mp[num - mp[num - 1]] = mp[num]
            mp[num + mp[num + 1]] = mp[num]

            res = max(res,mp[num])
    return res  


        