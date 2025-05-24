# 2 pointer approach 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.strip()
        left = 0
        right = len(s) -1 
        while left <= right:
            if s[left] != s[right]:
                return False 
            left += 1 
            right -= 1 
        return True 
    

# recursion pseudocode 

def recur(s,n,i):
    if i >= n//2:
        return True 

    if s[i] != s[n-i-1]:
        return False 

    recur(i+1)


def main():
    s = str(input('enter the input string:'))
    n = len(s)
    recur(s,n,0)

#inbuilt functions 

def isPalindrome(self, s: str) -> bool:
        newstr = ''

        for c in s:
            if c.isalnum():
                newstr += c.lower()
        if newstr == newstr[::-1]:
            return True 
        else:
            return False 
        
# constant memory 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s) - 1
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1 
            while r > l and not self.alphanum(s[r]):
                r -= 1 

            
            if s[l].lower() != s[r].lower():
                return False 
            
            l , r = l + 1 , r - 1
        return True
    def alphanum(self,c):
        return (ord('A') <= ord(c) <= ord('Z') or   
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
