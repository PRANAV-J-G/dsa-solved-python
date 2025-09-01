def longest_unique_subarray(nums):
    seen = set() 
    left = 0 
    max_len = 0 

    for right in range(len(nums)):
        if nums[right] in seen:
            seen.remove(nums[left])
            left += 1
        seen.add(nums[right])
        max_len = max(max_len,right - left + 1)
    
    return max_len 



