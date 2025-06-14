# sorting (O(m*nlogn))
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
    

# without using default dict 
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = {}

        for s in strs:
            sorteds = ''.join(sorted(s))

            if sorteds in res:
                res[sorteds].append(s)
            else:
                res[sorteds] = [s] 
        return list(res.values())


# using hashmaps (brute force)
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

result = defaultdict(list)
print(result)