# solution with exceeded time limit 
def divisor(n):
        	#code here
    total = []
    for i in range(1,n+1):
        for j in range(1,i+1):
            if i % j == 0:
                total.append(j)
    return sum(total)

n = 10

divisor(n)

#optimal code
def sum_of_divisors(n):
    total = 0
    divisor_sum = [0] * (n + 1)  # Array to store the sum of divisors for each number
    
    # For each number from 1 to n, add it as a divisor to all of its multiples
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):  # j is a multiple of i
            divisor_sum[j] += i
    
    # Sum up all the divisor sums
    total = sum(divisor_sum)
    return total


x = 10

sum_of_divisors(x)



#best option 

def sumdivi(n):
    ans = [0] * (n+1)

    for i in range(1,n+1):
        count = n // i 

        ans[i] = i * count
    return sum(ans) 
n = 5 
sumdivi(n)


