from typing import List 
class Solution:
    def binary2dsearch(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1
        
        while left <= right:
            mid = (left + right) // 2
            row = mid // cols 
            col = mid % cols
            value = matrix[row][col]
            
            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1
    
        return False    


# search in a 2D matrix 2 ,  where all the rows of the matrix are individually sorted 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False 
        row = 0 
        col = len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False
