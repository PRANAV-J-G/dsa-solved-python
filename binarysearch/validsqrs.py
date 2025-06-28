# optimal approach using binary search 
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        
        left , right = 2 , num // 2

        while left <= right:
            mid = (left + right) // 2
            squared = mid * mid

            if squared == num:
                return True
            elif squared < num:
                left = mid + 1
            else:
                right = mid - 1 
        return False
    
# better solution
def better(num):
    return (num**0.5)%1 == 0

num = 16
print(better(num))
