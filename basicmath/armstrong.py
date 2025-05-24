def armstrong(n): 
    sum = 0 
    dup = n 
    length = len(str(n))
    print(length)
    while n > 0:
        last_digit = n%10
        sum = sum + (last_digit**length)
        n = n//10
    
    if dup == sum:
        return True 
    else: 
        return False

 
n = 1634

print(armstrong(n))


# time complexity = O(n*log(N)) for the worst 
# space complexity for worst case O(N) because of the extra array taken in the merge function 