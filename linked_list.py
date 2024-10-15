# Define the Node class for a singly linked list
class Node:
    # Constructor for the Node class
    def __init__(self, value):
        # Set the value attribute for the Node
        self.value = value
        # Initialize the next attribute to None
        self.next = None
 
# Define the LinkedList class
class LinkedList:
    # Constructor for the LinkedList class
    def __init__(self, value):
        # Create a new Node with the given value
        new_node = Node(value)
        # Set the head attribute to the new Node
        self.head = new_node
        # Set the tail attribute to the new Node
        self.tail = new_node
        # Initialize the length attribute to 1
        self.length = 1

    def print_list(self):
        # Set a temporary pointer (temp) to the head of the list to start traversal 
        temp = self.head
 
        # Iterate through the list until the end (temp is None)
        while temp is not None:
            # Print the value of the current node (temp)
            print(temp.value)
    
            # Move the temporary pointer (temp) to the next node in the list
            temp = temp.next
    
    def append(self, value):
        # Create a new node with the given value
        new_node = Node(value)
    
        # Check to see if the linked list is empty
        if self.head is None:
            # Point both head and tail at the new node
            self.head = new_node
            self.tail = new_node
        else:
            # Point the next pointer of the last node at the new node
            self.tail.next = new_node
            # Point tail at the new node
            self.tail = new_node
    
        # Increment the length of the linked list
        self.length += 1
    
    def pop(self):
        if self.length == 0:
            return None
        
        if self.length == 1:
            temp = self.tail
            self.head = None
            self.tail = None
            self.length -= 1 
            return temp
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            last_node = self.tail
            temp.next = None
            self.tail = temp
            self.length -= 1 
            return last_node
    
    # Define the prepend method for the LinkedList class
    def prepend(self, value):
        # Create a new Node with the given value
        new_node = Node(value)
        
        # Check if the linked list is empty
        if self.length == 0:
            # Set the head and tail attributes to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # Set the next attribute of the new node to the current head
            new_node.next = self.head
            # Update the head attribute to the new node
            self.head = new_node
            
        # Increment the length attribute of the LinkedList
        self.length += 1
        
        # Return True to indicate a successful operation
        return True 
    
    def pop_first(self):
        if self.length == 0:
            return None
        
        if self.length == 1:
            first_node = self.head 
            self.head = None
            self.tail = None
            self.length -= 1 
            return first_node
        else:
            first_node = self.head 
            self.head = self.head.next
            first_node.next = None
            self.length -= 1 
            return first_node 
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1   
        return True  

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp