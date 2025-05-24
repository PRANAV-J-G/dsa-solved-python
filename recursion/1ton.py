def nums(n):

    if n == 0:
        return
    nums(n-1)

    print(n,end=' ')

n = 10 

nums(n)

# As the stack unwinds , the function resumes where it left off 
# printNos(1) resumes and prints 1.
# printNos(2) resumes and prints 2.
# printNos(3) resumes and prints 3.
