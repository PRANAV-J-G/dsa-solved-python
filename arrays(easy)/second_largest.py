 #brute force solutions 
def brute_one(arr):
    arr.sort()
    largest = arr[-1]
    for i in range(len(arr)-2,-1,-1):
        if arr[i] < largest:
            return arr[i]
    return None

arr = list(map(int,input().split()))
print(brute_one(arr))

#brute force solution two 
def brute_two(arr):
    arr.sort()
    largest = arr[-1]

    filtered = [x for x in arr if x != largest]
    filtered.sort()
    second = max(filtered)
    if not filtered:
        return None
    return second

question = list(map(int,input().split()))
print(brute_two(question))

#better solution O(2N)
def second(arr):
    largest = arr[0]
    second_largest = -1 #assuming all the elements of the array are positive 
    for i in arr:
        if i > largest:
            largest = i 
    for j in arr:
        if j > second_largest and j != largest:
            second_largest = j
    return second_largest
example = list(map(int(input().split())))
print(second(example))

#optimal solution O(
def optimal(arr):
    largest = arr[0]
    second_largest = -999
    for i in arr:
        if i > largest:
            second_largest = largest 
            largest = i 
        elif i < largest and i > second_largest:
            second_largest = i
    return second_largest
example = list(map(int,input().split()))
print(optimal(example))