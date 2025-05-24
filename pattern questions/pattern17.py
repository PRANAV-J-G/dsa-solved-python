def pattern17(n):
    for i in range(n): 
        #spaces 
        for j in range(n-i-1):
            print(' ',end=' ')

        char = chr(65)
        k = 0
        breakpoint = (2*i+1)//2
        for j in range(2*i+1):
            print(char,end=' ')
            if j < breakpoint:
                k += 1
                char = chr(65+k)
            else:
                k-=1
                char = chr(65+k)
                


        #spaces
        for j in range(n-i-1):
            print(' ',end=' ')

        print()  




n = 5 
print(pattern17(n))