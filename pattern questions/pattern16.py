def pattern16(n):
    for i in range(n):
        ch = chr(65+i)
        for j in range(i+1):
            print(ch,end=' ')
        print()
    
n =5
print(pattern16(n))