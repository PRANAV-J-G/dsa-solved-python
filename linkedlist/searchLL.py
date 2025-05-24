class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

class Solution:
    def search(self,head,val): 
        current = head 

        while current:
            if current.data == val:
                return True
            current = current.next
        return False
class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self,data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node 

    
ll = linkedlist()  # Create a new linked list
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

val = 4 
s = Solution()

ans = s.search(ll.head,val)

print(ans)

