# leader - every element to the right of an element must be smaller
def brute(nums):
    ans = []
    for i in range(len(nums)):
        leader = True 

        for j in range(i+1,len(nums)):
            if nums[j] > nums[i]:
                leader =  False
                break 
        if leader == True:
            ans.append(nums[i])
    return ans 
nums = [6,22,12,0,6]
print(brute(nums))  #nearly o(n**2)


# optimal solution 
import sys
def optimal(nums):
    ans = []
    maxi = -sys.maxsize
    for i in range(len(nums)-1,-1,-1):
        if nums[i] > maxi:
            ans.append(nums[i])
        maxi = max(maxi,nums[i])

    ans.reverse() # O
    return ans

nums = [6,22,12,0,6]

print(optimal(nums))    
