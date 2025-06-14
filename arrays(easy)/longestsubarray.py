# longest subarray with sum = k [positives only]

def brute(arr,k):
    n = len(arr)
    length = 0
    for i in range(n):
        s= 0
        for j in range(i,n):

            s += arr[j]
            if s == k:
                length = max(length,j-i+1)
    return length   


arr = [1,2,3,1,1,1,1,4,2,3]
k = 4
print(brute(arr,k))