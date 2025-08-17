def nthroot(n,m):
    def func(mid,n,m):
        ans = 1
        for i in range(1,n+1):
            ans = ans * mid
            if ans > m:
                return 2
            elif ans == m:
                return 1
        return 0
    left = 0 
    right = m
    while left <= right:
        mid = (left+right) // 2
        midN = func(mid,n,m)
        if midN == 1:
            return mid
        elif midN == 0:
            left = mid + 1
        else:
            right = mid - 1
    return -1
m = 27
n = 3
print(nthroot(n,m))
        