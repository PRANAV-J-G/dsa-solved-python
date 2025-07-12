import sys
# intuition just return the index of the minumum element which must be the number of times an array is rotated 
def optimal(nums):
    left, right = 0, len(nums) - 1
    index = -1
    ans = sys.maxsize

    while left <= right:
        # If subarray is sorted
        if nums[left] <= nums[right]:
            if nums[left] < ans:
                ans = nums[left]
                index = left
            break  # no need to search further

        mid = (left + right) // 2

        # Check left part is sorted
        if nums[left] <= nums[mid]:
            if nums[left] < ans:
                ans = nums[left]
                index = left
            left = mid + 1  # move right
        else:
            if nums[mid] < ans:
                ans = nums[mid]
                index = mid
            right = mid - 1  # move left

    return index


def count_rotations_with_duplicates(nums):
    left, right = 0, len(nums) - 1
    index = -1
    ans = int('inf')

    while left <= right:
        # If subarray is sorted
        if nums[left] < nums[right]:
            if nums[left] < ans:
                ans = nums[left]
                index = left
            break

        mid = (left + right) // 2

        # Check if mid is minimum
        if nums[mid] < ans:
            ans = nums[mid]
            index = mid

        # Can't decide, so move left & right inward
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
        elif nums[left] <= nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return index
