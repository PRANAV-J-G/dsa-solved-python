'''floor = smallest number in the array that is <= x 
ceil = largest number in the array that is >= x
'''

def floor_binary_search(nums, target):
    left, right = 0, len(nums) - 1
    floor_val = -1  # default if no floor exists

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return nums[mid]  # exact match is the floor
        elif nums[mid] < target:
            floor_val = nums[mid]  # potential floor, but maybe there's a larger one
            left = mid + 1
        else:
            right = mid - 1

    return floor_val

    return floor_val 
    return floor_val 
