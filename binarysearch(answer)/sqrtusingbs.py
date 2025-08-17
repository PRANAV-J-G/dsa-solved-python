def sqrt(target):
    left,right = 0,target
    ans = 0
    while left <= right:
        mid = (left+right)//2

        if mid*mid <= target:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans

target = 28 
print(sqrt(target))
        