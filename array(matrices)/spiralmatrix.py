# only one solution 
# only optimal solution 
# tc and sc = O(n*m)
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        left = 0 
        right = m - 1
        top = 0 
        bottom = n - 1
        ans = []

        while left <= right and top <= bottom:
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top += 1 

            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right,left-1,-1):
                    ans.append(matrix[bottom][i])
                bottom -= 1
            
            if left <= right:
                for i in range(bottom,top-1,-1):
                    ans.append(matrix[i][left])
                left += 1
        return ans  


# spiral matrix 2 

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left = 0
        right = n - 1
        top = 0 
        bottom = n - 1
        matrix = [[0] * n for _ in range(n)]
        num = 1
        while left <= right and top <= bottom:
            for i in range(left,right+1):
                matrix[top][i] = num
                num += 1
            top += 1
        
            for j in range(top,bottom+1):
                matrix[j][right] = num
                num += 1
            right -= 1

            if top <= bottom:
                for i in range(right,left-1,-1):
                    matrix[bottom][i] = num 
                    num += 1
                bottom -= 1

            if left <= right:
                for i in range(bottom,top-1,-1):
                    matrix[i][left] = num
                    num += 1

                left += 1
        return matrix