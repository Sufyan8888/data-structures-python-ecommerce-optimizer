# Define a Node class for the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Stores the data
        self.next = None  # Pointer to the next node


# Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None  # Head of the list (first node)

    # Method to add a new node at the end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:  # If list is empty, make the new node the head
            self.head = new_node
        else:
            last = self.head
            while last.next:  # Traverse to the end of the list
                last = last.next
            last.next = new_node  # Append the new node at the end

    # Method to print the linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Create a linked list for inventory management
inventory = LinkedList()

# Add inventory items
inventory.append("Item A")
inventory.append("Item B")
inventory.append("Item C")

# Print the current inventory
inventory.print_list()  # Outputs: Item A -> Item B -> Item C -> None

# Adding a new item to the inventory
inventory.append("Item D")
inventory.print_list()  # Outputs: Item A -> Item B -> Item C -> Item D -> None
