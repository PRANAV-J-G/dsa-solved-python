def brute(arr):
    n = len(arr)
    for i in range(1,n+2):
        flag = 0 

        for j in range(0,n):
            if arr[j] == i:
                flag = 1 
                break 
        if flag == 0:
            return i
    
arr = [1,2,3,4,5,6,7]

#print(brute(arr))


# use hashing techniques 

def better(nums):
    n = len(nums)
    hash = [0] * (n+2)

    for num in nums:
        hash[num] = 1

    for i in range(1,n+2):
        if hash[i] == 0:
            return i 

nums = [0,1,2,3,4,6,7]
print(better(nums))

# optimal approach 

def optimal(nums):
    n = len(nums)
    res = (n*(n+1)/2) - sum(nums)

    return int(res) 
nums = [0,1,2,3,4,6,7]
print(optimal(nums))

# XOR ( bit manipulation) i^i = 0   i^j = 1

def xor(nums):
    n = len(nums)
    xor1 = xor2 = 0
    for i in range(0,n):
        xor2 = xor2^ nums[i]
        xor1 = xor1 ^ (i+1)

    return xor1 ^ xor2 

nums = [0,1,2,3,4,6,7]
print(xor(nums))