def brute(arr):
    n = len(arr)
    for i in range(1,n+2):
        flag = 0 

        for j in range(0,n):
            if arr[j] == i:
                flag = 1 
                break 
        if flag == 0:
            return i
    
arr = [1,2,3,4,5,6,7]

print(brute(arr))