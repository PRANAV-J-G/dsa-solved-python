from typing import concat
class Solution:
    def countAndSay(self, n: int) -> str:
        result = '1'

        for i in range(n-1):
            curr = ''
            left = 0 

            while left < len(result):
                count = 1

                while left + 1 < len(result) and result[left] == result[left+1]:
                    left += 1
                    count += 1

                curr += concat(str(count),result[left])
                left += 1
            result = curr 
        return result 