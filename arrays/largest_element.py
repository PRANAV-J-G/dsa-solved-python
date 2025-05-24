from typing import List

#brute force solution
def brute(arr):
    arr.sort()
    print(arr)
    print('the largest element in array is',arr[-1])
arr=list(map(int,input().split()))
brute(arr)


#optimal solution
def largest(arr : List[int]) -> int:
    # code here 
    max_ele = 0
    for i in arr:
        if i > max_ele:
            max_ele = i
    return max_ele 

arr = list(map(int,input().split()))
print(largest(arr))

