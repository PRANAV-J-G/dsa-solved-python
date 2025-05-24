def reverse(n):
    revN = 0 
    X = abs(n)

    sign = 1 if n > 0 else -1 

    while X > 0 :
        last_digit = X % 10 
        revN = (revN * 10) + last_digit

        X = X // 10 
    return revN * sign 

n = -7789 
print(reverse(n))

