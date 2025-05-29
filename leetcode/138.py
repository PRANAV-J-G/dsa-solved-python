def brute(arr):
    n = len(arr)
    for i in range(n):
        num = arr[i]
        count = 0
        for j in range(n):
            if arr[j] == num:
                count += 1
        if count == 1:
            return num

arr = [1,1,2,2,3,3,4,4,5,5,6,7,7]
print(brute(arr))


# better solution 
# tc = o(3n) and sc = depends on the maximum element 
def better(arr):
    n = len(arr)
    maxi = 0
    for i in range(n):
        maxi = max(maxi,arr[i])
    hash = [0] * (maxi + 1)

    for num in arr:
        hash[num] += 1 
    
    for num in arr:
        if hash[num] == 1:
            return num
        
arr = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8]
print(better(arr))


def optimal(arr):
# using xor operations returns 0 if the numbers are the same and return the number itself if xor'ed with 0    
    xor = 0 
    for num in arr:
        xor = xor^num

    return xor 
arr = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8]
print(better(arr))