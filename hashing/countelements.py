'''Hashing refers to prestoring and fetching'''

# brute   tc = O(q * n)
def brute(arr,n):
    count = 0 
    for i in range(len(arr)):
        if arr[i] == n:
            count = count + 1
    
    return count 

number = 5 

arr = [1,2,3,4,5,6,7,8,5,5,5]

print(brute(arr,number))


# hashing 

class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr):
        #  code here
        maximum = max(arr)
        hash = [0] * (maximum+1)
        for i in arr:
            hash[i] += 1 
        return hash[1:]

s = Solution()
arr = [1,2,3,4,55,6]
print(s.frequencyCount(arr))

# using dictionary 

class Solution:
    # Function to count the frequency of all elements in the array using a hash map
    def frequencyCount(self, arr):
        # Create a dictionary to store frequencies
        frequency = {}
        
        # Count the occurrences of each element
        for num in arr:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        return frequency
# 10*6 is the max array size in the main function and 10*7 is the max size globally , else memory error(segmentation fault)


# collision = ????