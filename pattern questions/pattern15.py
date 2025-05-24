def patter15(n):
    for i in range(1,n+1):
        for j in range(n-i+1):
            print(chr(65+j),end=' ')
        print()

n = 5 
print(patter15(n))

# ABCDE
# ABCD
# ABC
# AB
# A