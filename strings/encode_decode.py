class Solution:
    def encode(self,strs):
        res = ''
        for s in strs:
            res = ''
            res += str(len(s)) + '#' + s
        return res 
    
    def decode(self,str):
        res , i = [] , 0

        while i < len(str):
            j = i 

            while j != '#':
                j += 1 
            length = str[i:j]

            res.append(str[j+1:j+1+length])