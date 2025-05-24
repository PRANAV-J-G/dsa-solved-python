# takes an element and inserts it in the correct position 

class Solution:
    def insertionSort(self, arr):
        #code here
        n = len(arr)
        for i in range(n):
            j = i 
            while j > 0 and arr[j-1] > arr[j]:
                arr[j-1],arr[j] = arr[j] , arr[j-1]
                j -= 1
        return arr 
    
# time complexity = O(n^2)

s = Solution()
arr = list(map(int,input().split()))
print(s.insertionSort(arr))