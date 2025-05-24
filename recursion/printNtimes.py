def ntimes(n):
    if n == 0:
        return
    ntimes(n-1)
    print('Pranav',end = ' ')

n = 4
ntimes(n)

