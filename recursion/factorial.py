def factorial(n):
    if n == 0:
        return 1 
    return n * (n-1)

n = 5 
print(factorial(n))


# class Solution:
#     def factorialNumbers(self, n):
#     	#code here 
#     	result = []
#         current_factorial = 1 
#         index = 1
        
#         while current_factorial <= n:
#             result.append(current_factorial)
#             index += 1
#             current_factorial *= index
#         return result 


# class Solution:
#     def factorialNumbers(self, n):
#     	#code here 
#     	result = []
#         current_factorial = 1 
        
#         for i in range(1,n+1):
#             if current_factorial > n:
#                 break
#             result.append(current_factorial)
            
#             current_factorial *= i + 1
#         return result 


# def factorial_numbers(n):
#     # Base case: return an empty list if n < 1
#     if n < 1:
#         return []
    
#     # Recursive call to get the factorials for numbers smaller than n
#     smaller_factorials = factorial_numbers(n - 1)
    
#     # Calculate the next factorial
#     next_factorial = 1 if not smaller_factorials else smaller_factorials[-1] * len(smaller_factorials) + 1
    
#     # Add the next factorial to the list if it is <= n
#     if next_factorial <= n:
#         smaller_factorials.append(next_factorial)
    
#     return smaller_factorials

# # Example usage:
# n = 150
# print(f"Factorial numbers smaller than or equal to {n}: {factorial_numbers(n)}")


