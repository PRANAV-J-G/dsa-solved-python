from collections import UserList
class Solution:
    def canMakeArithmeticProgression(self, arr: UserList[int]) -> bool:
        arr.sort() 
        index = 1 
        diff = arr[1] - arr[0]
        n = len(arr)
        while index < n-1:
            if arr[index+1]  - arr[index] != diff:
                return False 
            index += 1 
        return True  
