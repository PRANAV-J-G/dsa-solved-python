from collections import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ord_t = ord(target) - ord('a')

        for i in range(len(letters)):
            l_ord = ord(letters[i]) - ord('a')

            if l_ord > ord_t:
                return letters[i]
        return letters[0]
    

