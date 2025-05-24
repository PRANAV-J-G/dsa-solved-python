def pattern19(n):
    space = 0
    for i in range(n):
        for j in range(1,n+1-i):
            print('*',end='')

        #space
        for j in range(space):
            print(' ',end='')
            
        for j in range(1,n+1-i):
            print('*',end='')
        space += 2
        print()

    spaces = 2*n -2 
    for i in range(1,n+1):
        for j in range(1,i+1):
            print('*',end='')

        #space
        for j in range(spaces):
            print(' ',end='')
            
        for j in range(1,i+1):
            print('*',end='')

        spaces -= 2
        print()
n = 5
print(pattern19(n)) 


# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********