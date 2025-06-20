# longest subarray with the sum k [only positives] tc = O(n*2)

def brute(nums,k):
    length = 0
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            s = 0
            for m in range(i,j):
                s += nums[m]

                if s == k:
                    length = max(length,j - i + 1)
    return length
nums = [3,3,4,5,5,2,1,31,34]
target = 20
print(brute(nums,target))


# better solution using hashing 
 



                