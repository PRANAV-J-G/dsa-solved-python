# using normal hashing 
def charhash(arr):
    n = len(arr)
    hash  = [0] * 26

    for i in range(len(arr)):
        hash[ord(arr[i]) - ord('a')] += 1

    return hash

arr = 'pranavjg'
print(charhash(arr))

#using dictionary 

def hashing(arr):

    hash = {chr(i): 0 for i in range(ord('a'),ord('z')+1) }

    for char in arr:
        hash[char] += 1
    
    return hash 

arr = 'pranav'


print(hashing(arr))
# hash maps takes logN time for fetching as well as storing 
