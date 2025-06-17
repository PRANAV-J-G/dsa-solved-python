class Solution:
    def encode(self,strs): # join all the strings to a single string
        res = '' # create a empty string 
        for s in strs: # iterate through each str in the list of strings
            res += str(len(s)) + '#' + s  # create a delimiter to recognize the strings (like : 4#milk 4 - lenght # identifier)
        return res # return as a single string 
    
    def decode(self,str):
        res , i = [] , 0 # create a empty list to store and a pointer 

        while i < len(str):
            j = i # initialize another pointer

            while j != '#': # to check for the delimiter in the strings 
                j += 1  # move the pointer to the delimiter
            length = int(str[i:j]) # find 

            res.append(str[j+1:j+1+length])

            i = j + 1 + length