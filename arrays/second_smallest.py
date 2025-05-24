#brute force and better solutions are similiar to second_smallest element questions 
import sys

#optimal 
def optimal(arr):
    smallest = arr[0]
    second_smallest = sys.maxsize
    for i in arr:
        if i < smallest:
            second_smallest = smallest 
            smallest = i 
        elif i != smallest and i < second_smallest:
            second_smallest = i
    return second_smallest
example = list(map(int,input().split()))
print(optimal(example))