n = 5
for i in range(1,n+1):

    for j in range(n-i+1):
        print('*',end='')
    print()

# *****
# ****
# ***
# **
# *

# printing numbers in decrement 

n = 5

for i in range(1,n+1):

    for j in range(1,n-i+2):
        print(j,end='')
    print()