class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None 
        else:       
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None      
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev  
        return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        
        self.length += 1   
        return True  

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
 
        temp = self.get(index)
        
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
 
        self.length -= 1
        return temp
        
    def reverse(self):
        temp = self.head
        while temp is not None:
            # swap the prev and next pointers of node points to
            temp.prev, temp.next = temp.next, temp.prev
            
            # move to the next node
            temp = temp.prev
            
        # swap the head and tail pointers
        self.head, self.tail = self.tail, self.head
        
    def is_palindrome(self):
        # 1. If the length of the doubly linked list is 0 or 1, then 
        # the list is trivially a palindrome. 
        if self.length <= 1:
            return True
        
        # 2. Initialize two pointers: 'forward_node' starting at the head 
        # and 'backward_node' starting at the tail.
        forward_node = self.head
        backward_node = self.tail
        
        # 3. Traverse through the first half of the list. We only need to 
        # check half because we're comparing two nodes at once: one from 
        # the beginning and one from the end.
        for i in range(self.length // 2):
            # 3.1. Compare the values of 'forward_node' and 'backward_node'. 
            # If they're different, the list is not a palindrome.
            if forward_node.value != backward_node.value:
                return False
            
            # 3.2. Move the 'forward_node' one step towards the tail and 
            # the 'backward_node' one step towards the head for the next iteration.
            forward_node = forward_node.next
            backward_node = backward_node.prev
    
        # 4. If we've gone through the first half of the list without 
        # finding any non-matching node values, then the list is a palindrome.
        return True
    
    def swap_pairs(self):
        # Step 1: Initialize a dummy node to act as a placeholder
        # for the start of the list.
        dummy_node = Node(0)
    
        # Connect this dummy node to the actual head of the list.
        # This simplifies the swapping process.
        dummy_node.next = self.head
    
        # Step 2: Initialize 'previous_node' to 'dummy_node'.
        # This helps us remember the node just before the pair
        # we are about to swap.
        previous_node = dummy_node
    
        # Step 3: Loop through the list as long as there are pairs
        # of nodes available to swap.
        while self.head and self.head.next:
    
            # Identify the first node in the pair to be swapped.
            first_node = self.head
    
            # Identify the second node in the pair to be swapped.
            second_node = self.head.next
    
            # Update 'previous_node' to point to 'second_node',
            # effectively skipping over 'first_node'.
            previous_node.next = second_node
    
            # Connect 'first_node' to the node that comes after
            # 'second_node'. This ensures we don't lose the
            # rest of the list.
            first_node.next = second_node.next
    
            # Swap 'first_node' and 'second_node' by connecting
            # 'second_node' back to 'first_node'.
            second_node.next = first_node
    
            # Update the 'prev' pointers for both 'first_node'
            # and 'second_node' to maintain the doubly-linked
            # structure.
            second_node.prev = previous_node
            first_node.prev = second_node
    
            # If there's a node after 'first_node', update its
            # 'prev' to point back to 'first_node'.
            if first_node.next:
                first_node.next.prev = first_node
    
            # Move the 'head' to the node just after 'first_node'
            # to prepare for the next iteration.
            self.head = first_node.next
    
            # Update 'previous_node' to point to 'first_node'
            # for the next pair to swap.
            previous_node = first_node
    
        # After the loop, set the new head of the list to the
        # node that comes after 'dummy_node'.
        self.head = dummy_node.next
    
        # Make sure the new head's 'prev' is set to None, as it
        # is now the first node in the list.
        if self.head:
            self.head.prev = None




my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)

print('DLL before remove():')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(2).value)
print('DLL after remove() in middle:')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(0).value)
print('DLL after remove() of first node:')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(2).value)
print('DLL after remove() of last node:')
my_doubly_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    DLL before remove():
    1
    2
    3
    4
    5

    Removed node:
    3
    DLL after remove() in middle:
    1
    2
    4
    5

    Removed node:
    1
    DLL after remove() of first node:
    2
    4
    5

    Removed node:
    5
    DLL after remove() of last node:
    2
    4

"""

