n = 5 

for i in range(n):
    for j in range(i):
        print(' ',end='')
    for j in range(2*n-(2*i+1)):
        print('*',end='')
    for j in range(i):
        print(' ',end='')
    print()


# *********
#  ******* 
#   *****
#    ***
#     *  
print('-----------------------------')
n = 5
for i in range(n):
    for j in range(n-i-1):
        print(' ',end='')
    for j in range(2*i+1):
        print('*',end='')
    for j in range(n-i+1):
        print(' ',end='')
    print()
for i in range(n):
    for j in range(i):
        print(' ',end='')
    for j in range(2*n-(2*i+1)):
        print('*',end='')
    for j in range(i):
        print(' ',end='')
    print()


'''
    Time Complexity - O( N * N )
    Space Complexity - O( 1 )

    where N is the given input.
'''


def nStarDiamond(n: int) -> None:

    # Initialise 'gap' and 'stars'.
    gap = n-1
    stars = 1
    for i in range(n):
        for j in range(gap):
            print(' ', end="")
        for j in range(gap, gap+stars):
            print('*', end="")

        # End the current row of the pattern.
        print()

        gap -= 1
        stars += 2

    gap = 0
    stars = 2 * n - 1
    for i in range(n, 2*n):
        for j in range(gap):
            print(' ', end="")
        for j in range(gap, gap+stars):
            print('*', end="")

        # End the current row of the pattern.
        print()

        gap += 1
        stars -= 2
