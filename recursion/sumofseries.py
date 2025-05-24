def sum_series(n):
    # Base case: when n is 1, the first term is 13
    if n == 1:
        return 1
    # Recursive case: calculate the nth term and add it to the sum of the series up to (n-1)
    return (n**3) + sum_series(n - 1)

# Example usage:
n = 5
print(f"The sum of the series up to the {n}-th term is: {sum_series(n)}")
