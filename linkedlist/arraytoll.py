class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def array(self,arr):
        if not arr:
            return None
        
        head = Node(arr[0])
        current = head 

        for val in arr[1:]:
            current.next = Node(val)
            current = current.next
        return head
    
arr = [2,3,4,5]
s = Solution()
head = s.array(arr)

current = head 

while current:
    print(current.data, end = '->')
    current = current.next 





