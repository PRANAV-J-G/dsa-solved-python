def pattern18(n):
    for i in range(1,n + 1):  # Loop for rows
        for j in range(i):  # Loop for columns in each row
            print(chr(65 + n - 1 - j), end=' ')  # Start from 'C' and decrement
        print()  # Move to the next line

n = 5
print(pattern18(n))

# E 
# E D 
# E D C
# E D C B
# E D C B A


def alpha(n):
    for i in range(n):
        for j in range(n-i-1,n):
            print(chr(65+j),end='')
        print()

n = 4
print(alpha(n))
