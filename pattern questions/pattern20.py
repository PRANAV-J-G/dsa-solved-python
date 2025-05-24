def pattern20(n):
    space = 2*n-2
    #stars
    for i in range(1,2*n):
        #stars
        stars = i if i < n else 2 * n- i 
        for j in range(1,stars+1):
            print('*',end='')
        #spaces
        for j in range(1,space+1):
            print(' ',end='')
        
        #stars 
        for j in range(1,stars+1):
            print('*',end='')
            
        print() 
        if i < n:
            space -= 2 
        else: 
            space += 2
        

n = 5
print(pattern20(n))
             
