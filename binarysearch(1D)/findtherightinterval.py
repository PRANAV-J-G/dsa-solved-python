# intuition (store the starts in a dict and sort them to preserve the index)
# then perform binary search in the dict to points in sorted starts list using the end of every interval 

def binary(intervals):
    starts = {interval[0]:i for i,interval in enumerate(intervals)}
    sorted_starts = sorted(starts.keys())
    result = []
    for interval in intervals:
        end = interval[1]
        answer = -1
        left , right = 0 ,len(intervals) - 1

        while left <= right:
            mid = (left + right) // 2

            if sorted_starts[mid] >= end:
                answer = mid 
                right = mid -1
            else:
                left = mid + 1
            
        if answer == -1:
            result.append(-1)
        else:
            result.append(starts[sorted_starts[answer]])
    return result

intervals = [[3,4],[2,3],[1,2]]
print(binary(intervals))