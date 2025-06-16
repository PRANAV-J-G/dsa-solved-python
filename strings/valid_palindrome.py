# ordinary solution 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''

        for char in s:
            if char.isalnum():
                res += char.lower()
        
        if res == res[::-1]:
            return True 
        return False


# another way 

    def valindrome(s):
        l = 0 
        r = len(s) - 1

        while l < r:
            
            while l < r and not s[l].isalnum():
                l += 1
            
            while r > l and not s[r].isalnum():
                r -= 1 
            
            if s[l].lower() != s[r].lower():
                return False 
            
            l ,r = l + 1 , r - 1 
        return True 

    s = "A man, a plan, a canal: Panama"
    print(valindrome(s))



# valid palindrome 2 (palindrome with a character removed)

def valindrome2(s):
    l = 0 
    r = len(s) - 1

    while l < r: 
        if s[l] == s[r]:
            l += 1
            r -= 1 
        elif s[l+1:r+1] == s[l+1:r+1][::-1] or s[l:r] == s[l:r][::-1]:
            return True 
    return False