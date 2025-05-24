def palindrome(n):
    if n < 0:
        return False
    else: 
        return str(n) == str(n)[::-1]
    
n = 121
print(palindrome(n))