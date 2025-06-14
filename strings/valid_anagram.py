# Using the sorting approach 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort_s = sorted(s)
        sort_t = sorted(t)
        if sort_s == sort_t:
            return True 
        else:
            return False
        

# using the hashset approach 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        shash = {}
        thash = {}

        for letter in s:
            if letter in shash:
                shash[letter] += 1
            else:
                shash[letter] = 1


        for letter in t:
            if letter in thash:
                thash[letter] += 1
            else:
                thash[letter] = 1 
        
        return shash == thash
    

# using counters in python 
from collections import Counter
def anagram(s,t) -> bool:
    return Counter(s) == Counter(t)   

s = 'dog'
t = 'god'     

print(anagram(s,t))