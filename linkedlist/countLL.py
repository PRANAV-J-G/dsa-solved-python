class LinkedList:
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
    
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None



class Solution:
    def count(self,head):
        current = head
        count = 0 

        while current:
            count += 1 
            current = current.next
        return count 
    
ll = LinkedList()
ll.append(1)
ll.append(12)
ll.append(3)
ll.append(4)
ll.append(5)

sol = Solution()

node_count = sol.count(ll.head)
print(node_count)