from typing import List 
# brute force solution 
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)

        for i in range(n):
            if arr[i] <= k:
                k += 1
            else:
                break 
        return k
    

# better / optimal solution 
# using binary search 

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left , right = 0 ,len(arr)-1 
        while left <= right:
            mid = (left + right) // 2

            missing = arr[mid] - (mid + 1)

            if missing < k: left = mid+ 1
            else: right = mid - 1

        ans = right + 1 + k
        return ans 