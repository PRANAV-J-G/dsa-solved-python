# length of longest subarray with the sum k [only positives] tc = O(n*2)
from typing import List
def brute(nums,k):
    length = 0
    for i in range(len(nums)):
        s = 0
        for j in range(i,len(nums)):
            s += nums[j]

            if s == k:
                length = max(length,j - i + 1)
    return length
nums = [3,3,4,5,5,2,1,31,34]
target = 20
print(brute(nums,target))


# better solution using hashing  for only positives 
# becomes the optimal solution if both positives and negatives are present 
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        length = 0
        hashmap = {0: 1}  # prefix_sum -> frequency

        for i,num in enumerate(nums):
            prefix_sum += num
            
            if prefix_sum - k in hashmap:
                length = max(length,i - hashmap[prefix_sum - k])
            if prefix_sum - k not in hashmap:
                hashmap[prefix_sum] = i
            
        return length
            

nums = [1,2,3,1,1,1,1,4,2,3]
target = 3

s=Solution()
print(s.subarraySum(nums,target))


# optimal solution using two pointer for positives only and zeros

def optimal(nums,k):
    left , right = 0 
    maxlen = 0 
    sum = nums[0]
    n = len(nums) 

    while right < n:

        while left <= right and sum > k:
            sum -= nums[left]
            left += 1
        
        if sum == k:
            maxlen = max(maxlen,right-left+1)

        right += 1

        if right <n: 
            sum += nums[right]

    return maxlen  

# count of subarray with sum k (only positives)
# for brute modify the length problem slightly 

# optimal sol for both negative and positives 
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        hashmap = {0:1}  # prefix_sum -> frequency

        for num in nums:

            prefix_sum += num 

            if prefix_sum - k in hashmap:
                count += hashmap[prefix_sum - k]

            if prefix_sum not in hashmap:
                hashmap[prefix_sum] = hashmap.get(prefix_sum,0) + 1

        return count    


                