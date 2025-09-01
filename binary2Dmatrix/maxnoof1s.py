from typing import List
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        

        def lowerbound(mat,cols,x):
            low = 0 
            high = cols - 1 
            ans = cols

            while low <= high:
                mid = (low + high) // 2
                if mat[mid] >= x:
                    ans = mid 
                    high = mid - 1
                else:
                    low = mid + 1
            return ans 
        rows = len(mat)
        cols = len(mat[0])
        cnt_max = -1
        index = -1
        for i in range(rows):
            first = lowerbound(mat[i],cols,1)
            ones_count = cols - first
            if ones_count > cnt_max:
                cnt_max = ones_count        
                index = i
        return [index,cnt_max]
        

