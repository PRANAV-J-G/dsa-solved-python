def nLetterTriangle(n: int) -> None:
    # Write your solution here.
    for i in range(1, n + 1):
        for j in range(i):  # Print 'i' letters in each row
            print(chr(65 + j), end=' ')  # Convert number to corresponding ASCII letter
        print()
    pass

n = 6 
print(nLetterTriangle(n))

