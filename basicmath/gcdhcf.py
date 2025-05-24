#gcd 

def gcd(n,m):
    mn = min(n,m)
    gcd = 1
    for i in range(1,mn+1):
        if n % i == 0 and m % i == 0:
            gcd = i 
    return gcd 

n=9
m=12
print(gcd(n,m))


# euclidean 

def euc(a,b):
    gcd = 1 
    while a > 0 and b > 0:
        if a > b:
            a = a % b 
        else:
            b = b % a 
        
        if a == 0:
            gcd = b 
        else:
            gcd = a 
    return gcd 

a = 9
b = 12

print(euc(a,b))


from collections import List
def lcmAndGcd(self, a : int, b : int) -> List[int]:
    # code here
    ans = [0] * (2)
    
    for i in range(1,min(a,b)+1):
        if a % i == 0 and b % i == 0:
            ans[1] = i #gcs 
    ans[0] = (a*b) // ans[1]  # lcm 

# Python Program to find the L.C.M. of two input number

def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 54
num2 = 24

print("The L.C.M. is", compute_lcm(num1, num2))
