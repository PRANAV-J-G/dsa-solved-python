def brute(nums): # tc = O(2n)
    positive = []
    negative = []

    for i in range(len(nums)):
        if nums[i] > 0:
            positive.append(nums[i])
        else:
            negative.append(nums[i])
    
    for i in range(len(nums)//2):
        nums[2*i] = positive[i]
        nums[2*i+1] = negative[i]
    
    return nums
nums = [3,1,-2,-5,2,-4]
print(brute(nums))


# slightly better 

def solution(nums):
    n = len(nums)
    ans = [0] * n
    negative = 1
    positive = 0
    for i in range(n):
        if nums[i] > 0:
            ans[positive] = nums[i]
            positive += 2
        else:
            ans[negative] = nums[i]
            negative += 2
    return ans 

nums = [3,1,-2,-5,2,-4]
print(solution(nums))


# if pos != negatives 

def optimal(nums):
    negative = []
    positive = []

    for i in range(len(nums)):
        if nums[i] > 0:
            positive.append(nums[i])
        else:
            negative.append(nums[i])

    if len(positive) > len(negative):
        for i in range(len(negative)):
            nums[2*i] = positive[i]
            nums[2*i+1] = negative[i]
        index = len(negative) * 2 

        for i in range(len(negative),len(positive)):
            nums[index] = positive[i]
            index += 1
    else:
        for i in range(len(positive)):
            nums[2*i] = positive[i]
            nums[2*i+1] = negative[i]
        index = len(positive) * 2

        for i in range(len(positive),len(negative)):
            nums[index] = negative[i]
            index += 1
    return nums

nums = [3,1,-2,-5,2,-4]
print(optimal(nums))


