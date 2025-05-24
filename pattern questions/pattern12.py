def numberCrown(n: int) -> None:
    # Write your solution here.
    space = 2* (n-1)
    print(space)
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end='')

        for j in range(1,space):
            print(' ',end='')


        for j in range(i,0,-1):
            print(j,end='')
        print()
        space -= 2

n = 4

print(numberCrown(n))


# 1     1
# 12   21
# 123 321
# 12344321