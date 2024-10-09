# Pick one of the abstract data structures mentioned in this section that you have not yet implemented
# Build a custom Python class that demonstrates its functionality 
# Compare your solution to: https://github.com/david-legend/python-algorithms/tree/main/data-structures/src


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.head is None

    def append(self, value):
        """Add a node at the end of the list"""
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node
        self.length += 1

    def prepend(self, value):
        """Add a node at the beginning of the list"""
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        """Insert a node at a specific position in the list"""
        if index < 0 or index > self.length:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            self.prepend(value)
        else:
            new_node = Node(value)
            current = self.head
            for i in range(index - 1):  # Traverse to the node before the insertion point
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.length += 1

    def remove(self, value):
        """Remove the first occurrence of a node with the specified value"""
        if self.is_empty():
            return None

        if self.head.value == value:
            self.head = self.head.next
        else:
            current = self.head
            while current.next and current.next.value != value:
                current = current.next
            if current.next is None:
                return None  # Value not found
            current.next = current.next.next  # Skip over the node to remove
        self.length -= 1

    def display(self):
        """Display the linked list"""
        if self.is_empty():
            print("List is empty")
        else:
            current = self.head
            while current:
                print(current.value, end=" -> ")
                current = current.next
            print("None")  # End of the list

    def size(self):
        """Return the size of the linked list"""
        return self.length


# Example usage
ll = LinkedList()

# Append items
ll.append("A")
ll.append("B")
ll.append("C")
ll.display()  # Output: A -> B -> C -> None

# Prepend item
ll.prepend("Start")
ll.display()  # Output: Start -> A -> B -> C -> None

# Insert item
ll.insert(2, "Middle")
ll.display()  # Output: Start -> A -> Middle -> B -> C -> None

# Remove item
ll.remove("Middle")
ll.display()  # Output: Start -> A -> B -> C -> None

# Check size
print(f"Size of the list: {ll.size()}")  # Output: Size of the list: 4