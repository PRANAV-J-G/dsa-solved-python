#brute force solution  tc = o(nlogn) + n  sc =o(n)

def brute(arr):
    n = len(arr)
    unique = set()
    unique_index = 0 

    for i in range(n):
        if arr[i] not in unique:
            unique.add(arr[i])
            arr[unique_index] = arr[i]
            unique_index += 1
    return unique_index

arr = list(map(int,input().split()))
print(brute(arr))


#optimal solution (2 pointer approach)  time complexity = O(N) SC = O(1)

def optimal(arr):
    i = 0 
    n = len(arr)
    for j in range(n):
        if arr[j] != arr[i]:
            arr[i+1] = arr[j]
            i += 1
    return (i+1)

nums = [0,0,1,1,2,2,3,3]
print(optimal(nums))