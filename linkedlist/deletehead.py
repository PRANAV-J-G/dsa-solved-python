class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def search(self, head, val):
        current = head  # Start from the head of the linked list

        # Traverse the linked list
        while current:
            if current.data == val:  # If we find the value, return True
                return True
            current = current.next  # Move to the next node

        return False  # If we finish the loop without finding the value, return False

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list
        self.tail = None  # Initialize the tail of the linked list

    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data

        if not self.head:  # If the list is empty, set the head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Link the last node to the new node
            self.tail = new_node  # Update the tail to the new node

    def remove_head(self):
        if self.head:
            self.head = self.head.next

            if not self.head:
                self.tail = None

# Test the code
ll = LinkedList()  # Create a new linked list
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

print("Before removing head:")
# Print the linked list to see the elements
current = ll.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

# Remove the head
ll.remove_head()

print("\nAfter removing head:")
# Print the linked list again to see the elements after removal
current = ll.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

