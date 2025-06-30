# basics using two pointer approach 
def reverse(arr):
    left = 0 
    right = len(arr) - 1 

    while left <= right:
        arr[left],arr[right] = arr[right],arr[left]
        left += 1 
        right -=  1

    return arr

arr = [1,2,3,4,5]

print(reverse(arr))


#  basic recursion 

def rev(l,r):
    if l >= r:
        return 

    arr[l],arr[r] = arr[r],arr[l]
    rev(l+1,r-1)

def main():
    arr = list(map(int,input().split()))
    n = len(arr)
    print(rev(0,n-1))

main()


# Using recursion 

class Solution:
    def reverseArray(self, arr,left = 0,right=None):
        if right is None:
            right = len(arr) - 1 
        
        if left >= right:
            return 
        
        arr[left],arr[right] = arr[right],arr[left]
        
        self.reverseArray(arr,left+1,right-1)
