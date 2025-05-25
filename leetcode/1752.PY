from collections import UserList
# check if array is sorted and rotated (forms an originally sorted array)
class Solution:
    def check(self, nums: UserList[int]) -> bool:

        n = len(nums)
        count  = 0 

        if n == 1 : return True
        for i in range(1,2*n):
            if nums[(i - 1) % n ] <= nums[i % n]:
                count += 1 
            else:
                count = 1
            if count == n:
                return True
        return False


        