
def fibonacci(n):
    if n == 0:
        return 0 
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


n = 8
fibo = fibonacci(n)
print(fibo)

def fib():
    a,b=0,1
    if n<=0:
        return 0
    for i in range(1,n):
        a,b =b,a+b
    return b
