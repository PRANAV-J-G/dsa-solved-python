# count the occurences of an element in an array 

def linear(nums,target):
    count = 0

    for i in range(len(nums)):
        if nums[i] == target:
            count += 1
    return count 

# optimal approach 

def occurences(nums,target):
    def firstindex(nums,target):
        left , right = 0 ,len(nums) - 1
        ans = -1

        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                ans = mid 
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return ans
    
    def lastindex(nums,target):
        left , right = 0 , len(nums) - 1
        ans = - 1

        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                ans = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return ans
    first = firstindex(nums,target)
    last = lastindex(nums,target)

    if first == -1 or last == -1:
        return 0 
    return last - first + 1

nums = [2,8,8,8,8,8,9,10]
target = 8

print(occurences(nums,target))