def q10(n)-> None:
    for i in range(1,2*n):
        stars = i if i <= n else 2*n-i
        for j in range(stars):
            print('*',end='')
        print()
    return 


n = 5 

print(q10(n))


# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *