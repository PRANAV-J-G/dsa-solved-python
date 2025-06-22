# brute optimal 
# this is the better solution , brute will be the same but with O(n**3)
def brute(nums):

    maxsum = float('-inf')

    for i in range(len(nums)):
        sum = 0 

        for j in range(i,len(nums)):
            sum += nums[j]
            maxsum = max(maxsum,sum)
    return maxsum 
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(brute(nums))


# optimal solution to return sum alone 
# kadane's algo 
def optimal(nums):

    maxsum = float('-inf')
    sum = 0
    for num in nums:
        sum += num
        maxsum = max(maxsum,sum)
        if sum < 0:
            sum = 0
    return maxsum 
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(optimal(nums))


# print the subarray with the max sum 

def subarray(nums):
    maxsum = float('-inf')
    sum = 0 
    ansstart = -1
    ansend = -1
    for i in range(len(nums)):
        if sum == 0:
            start = i
        
        sum += nums[i]

        if sum> maxsum:
            maxsum = sum
            ansstart = start
            ansend = i

        if sum < 0:
            sum = 0
    print('the array is: [ ',end='')
    for i in range(ansstart,ansend+1):
        print(nums[i],end=' ')
    print(']')

    return maxsum    
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(subarray(nums))
