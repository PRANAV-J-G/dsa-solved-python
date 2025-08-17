class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[i] == s[j]:
                    substring = s[i:j+1]
                    if substring == substring[::-1] and len(substring) > len(longest):
                        longest = substring
        return longest

