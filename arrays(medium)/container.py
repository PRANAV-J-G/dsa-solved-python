def mostwater(height):
    left = 0 
    right = len(height) - 1 
    max_area = 0
    while left < right:
        curr = min(height[left],height[right])*(right - left) # because area = length * base 
        max_area = max(curr,max_area)


        if height[left] <= height[right]:
            left += 1 
        else:
            right -= 1
    
    return max_area
height = [1,7,2,5,4,6,3,6]

print(mostwater(height))


# brute force approach 
def brute(heights):
    res = 0 
    for i in  range(len(heights)):

        for j in range(i+1,len(heights)):
            curr = min(heights[i],heights[j])*(j-1)
            res = max(res,curr)
    return res
print(brute(height))

