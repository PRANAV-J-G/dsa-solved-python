def atoi(s):
    for char in s:
        result = 0
        sign = 1 

        if s[0] == '-' or s[0] == '+':
            if s[0] == '-':

                sign = -1
        if s[0] == '+':
            sign = 1
        
        s = s[1:]
        for char in s:
            if not char.isalnum():
                break 
            
            result = result * 10 + int(char)

        result = result * sign 
        return result 
        
string = '+1234'
print(atoi(string))


