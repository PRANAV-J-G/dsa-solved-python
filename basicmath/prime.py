
def prime(n):
    count = 0
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            count += 1
            if n/i != i:
                count += 1
    if count == 2:
        return 'Prime'
    else:
        return 'No'
#the for loop  runs for sqrt of the number itself 

n = 2

print(prime(n))