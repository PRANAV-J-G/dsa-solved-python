# parameterised recursion
def sumof(i,sum):
    if i < 0:
        print(sum)
        return 
    sumof(i-1,sum+i)

def main(n):
    sumof(n,0)

n = 15
main(n)

#functional recursion 
def upto(n):
    if n == 0:
        return 0 
    return n+upto(n-1)

n = 15
print(upto(n))