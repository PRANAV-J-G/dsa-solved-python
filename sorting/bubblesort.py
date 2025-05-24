'''pushes the maximun to the last by adjacent swaps'''

class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr):
        # code here
        n = len(arr)
        for i in range(n-1,0,-1):
            for j in range(0,i):
                if arr[j] > arr[j+1]:
                    arr[j+1],arr[j] = arr[j],arr[j+1]
        return arr
    
# time complexity O(n^2) --> worst complexity 



# optimized code 


def bubbleSort(arr):
        # code here
    swaps = 0
    n = len(arr)
    for i in range(n-1,0,-1):
        for j in range(0,i):
            if arr[j] > arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
                swaps += 1 
        if swaps == 0:
            break

    return arr

# BEST case of bubble sort time complexity o(n)
