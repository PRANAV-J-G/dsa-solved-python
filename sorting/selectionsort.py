

'''
step1: select minimums and then swap

Pseudocode: 

for i in range(n-2):
    min = i 
    for j in range(i,n):
        if arr[j] < arr[min]:
            min =j
    swap(i,min)

return arr
'''

# time complexity  = O(n^2) but exactly n^2/2 + n/2
class Solution: 
    def selectionSort(self, arr):
        n = len(arr)
        
        for i in range(n-1):
            mini = i 
            for j in range(i+1, n):  # Start from i+1 instead of i
                if arr[j] < arr[mini]:
                    mini = j  # Update minimum index
            
            # Swap only after finding the minimum in the rest of the array
            arr[i], arr[mini] = arr[mini], arr[i]
        
        return arr

s = Solution()
arr = list(map(int,input().split()))
print(s.selectionSort(arr))
