from numpy import double


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):

        new_node = Node(data)

        # case 1: list is empty
        if (self.head == None):
            self.head = new_node
            return
        
        # list has one or more nodes
        new_node.next = self.head 
        self.head.prev = new_node 
        self.head = new_node 

    def insert_at_end(self, data):

        new_node = Node(data)

        # case 1: list is empty
        if (self.head == None):
            self.head = new_node
            return
        
        # case 2: list has one node
        if (self.head.next == None):

            self.head.next = new_node
            new_node.prev =self.head
            return
        
        # case 3: list has one node and more than one node
        # loop to find reference of last node
        last_node = self.head
        while (last_node.next is not None):

            last_node = last_node.next
        
        # Attach the new node at the end
        last_node.next = new_node
        new_node.prev = last_node

    def insert_at_given_position(self, data, target_position):


        if (target_position <= 0):
            print("Invalid Position")
            return
        
        # when list is empty
        if (self.head == None and target_position != 1):
            print("Invalid position")
            return
        
        if (target_position == 1):
            self.insert_at_beginning(data)
            return

        # if (target_position > 2 and self.head.next == None):
        #     print("Invalid Position")
        #     return
        

        
        current_position = 1

        current_node = self.head

        while (current_node != None and current_position < target_position - 1):
            current_position = current_position + 1
            current_node = current_node.next

        if (current_node == None):
            print("Invalid Position")
            return
        

        new_node = Node(data)

        # when we inserting between two nodes ,we need these steps
        if (current_node.next != None):
            current_node.next.prev = new_node 
            new_node.next = current_node.next
            
        # these are needed
        current_node.next = new_node
        new_node.prev = current_node

    def delete_at_beginning(self):
        # case 1: List is empty
        if self.head == None:
            print ("List is empty")
            return
        
        # case 2: only one node is presnt
        if self.head.next == None:
            self.head = None
            return
        
        # case 3: we have 2 or more nodes
        self.head = self.head.next
        self.head.prev = None

        # case 3:  other way 
        """
        new_head = self.head.next
        new_head.prev = None
        self.head = new_head
        """

    def delete_at_end(self):
        # case 1: list is empty
        if self.head == None:
            print ("List is empty")
            return
        
        # case 2: list has only one node
        if self.head.next == None:
            self.head = None
            return
        
        # case 3:two or more nodes present in the list
        last_node = self.head

        # loop till to before last one node
        while last_node.next.next is not None:
            last_node = last_node.next
        
        last_node.next = None

    def delete_at_given_position(self, target_position):
        # case 1: List is empty
        if (self.head  == None):
            print("List is empty")
            return
        
        # case 2: position is invalid

        if (target_position <= 0):
            print(f"Invalid target Position: {target_position}")
            return
        
        # case 3: single node
        if ( self.head.next == None):
            self.head = None
            return
        
        # case 4: multi node
        to_be_deleted = self.head
        current_position = 1

        while(current_position < target_position and to_be_deleted is not None):
            current_position = current_position + 1
            to_be_deleted = to_be_deleted.next

        if to_be_deleted == None:
            print(f" Target position {target_position} is invalid, we have lesser nuber of node. ")
            return
        
        # case 4.1:  to_be_deleted node is the last node
        if (to_be_deleted.next == None):
            to_be_deleted.prev.next = None
            return
        
        # case 4.2: there are nodes after the to_be_deleted Node
        to_be_deleted.next.prev = to_be_deleted.prev
        to_be_deleted.prev.next = to_be_deleted.next
        # to_be_deleted.next = None


    def print_all_nodes_list(self):

        current_node = self.head

        while current_node is not None:

            print("<->",current_node.data, "<->", end=" ")

            current_node = current_node.next

        print("None")
    

    def print_backward(self):

        current_node = self.head

        if current_node is None:  # Empty list check
            print("List is empty")
            return
        
        # Traverse untill end node (last node)
        while current_node.next is not None:
            current_node = current_node.next

        # Step 2: Traverse backwards
        print("None", end=" ")
        while current_node is not None:

            print("<->", current_node.data, end=" ")

            current_node = current_node.prev

        print("<-> None")

    def search_key(self, key):
        if self.head is None: 
            print(f"Empty List: ", end=" ") # Empty list check
            print(f"{key} not found in list ❌")
            return
        
        current_node = self.head
        position = 1
        while current_node is not None:
            if (current_node.data == key):
                print(f"{key} found in list at {position} position ✅", end=" ")
                return
            
            current_node = current_node.next
            position += 1

        print(f"{key} not found in list ❌")
        
def insert_at_beggining_test_code(dlist: DoublyLinkedList):

    dlist.insert_at_beginning(10)
    dlist.insert_at_beginning(20)

    dlist.print_all_nodes_list()

    dlist.insert_at_beginning(5)
    dlist.print_all_nodes_list()

    dlist.print_backward()

def insert_at_end_test_code(dlist: DoublyLinkedList):
    dlist.insert_at_end(30)
    dlist.insert_at_end(40)
    dlist.insert_at_end(50)
    dlist.insert_at_end(60)

    dlist.print_all_nodes_list()

def insert_at_given_position_test_code(dlist: DoublyLinkedList):

    dlist.insert_at_given_position(10, -1)

    dlist.insert_at_given_position(10, 2)

    dlist.insert_at_given_position(10, 1)
    dlist.insert_at_given_position(20, 1)

    dlist.insert_at_given_position(30, 10)

    dlist.insert_at_given_position(30, 3)
    dlist.insert_at_given_position(40, 3)
    dlist.insert_at_given_position(50, 3)


    dlist.print_all_nodes_list()

def delete_at_beginning_end_test_code(dlist: DoublyLinkedList):
    # dlist.delete_at_beginning()
    # dlist.delete_at_end()

    
    # dlist.insert_at_beginning(40)
    # dlist.print_all_nodes_list()

    # dlist.delete_at_beginning()
    # dlist.print_all_nodes_list()

    # dlist.insert_at_end(50)

    # dlist.insert_at_end(10)
    # dlist.insert_at_end(20)
    # dlist.insert_at_end(30)
    # dlist.print_all_nodes_list()

    # dlist.delete_at_beginning()

    # dlist.print_all_nodes_list()

    # dlist.delete_at_end()
    # dlist.print_all_nodes_list()

    dlist.delete_at_beginning()
    dlist.delete_at_end()

    dlist.insert_at_beginning(10)
    dlist.delete_at_beginning()

    dlist.insert_at_end(20)
    dlist.delete_at_end()

    dlist.insert_at_beginning(10)
    dlist.insert_at_beginning(20)
    dlist.insert_at_beginning(30)
    dlist.insert_at_beginning(40)
    dlist.delete_at_end()

    dlist.print_all_nodes_list()

def delete_at_position_test_code(dlist: DoublyLinkedList):
    dlist.delete_at_given_position(-1)
    dlist.delete_at_given_position(1)

    dlist.insert_at_beginning(10)
    dlist.delete_at_given_position(-1)

    dlist.delete_at_given_position(1)
    
    dlist.insert_at_beginning(40)
    dlist.insert_at_beginning(30)
    dlist.insert_at_beginning(20)
    dlist.insert_at_beginning(10)

    dlist.print_all_nodes_list()

    dlist.delete_at_given_position(4)
    dlist.print_all_nodes_list()

    dlist.delete_at_given_position(2)
    dlist.print_all_nodes_list()

def print_all_nodes_test_code(dlist: DoublyLinkedList):
    dlist.insert_at_beginning(40)
    dlist.insert_at_beginning(30)
    dlist.insert_at_beginning(20)
    dlist.insert_at_beginning(10)

    dlist.print_all_nodes_list()

def serach_key_test_code(dlist: DoublyLinkedList):
    dlist.insert_at_beginning(40)
    dlist.insert_at_beginning(30)
    dlist.insert_at_beginning(20)
    dlist.insert_at_beginning(10)

    dlist.search_key(100)
    dlist.search_key(10)

if __name__ == "__main__":
    dlist =  DoublyLinkedList()
    # insert_at_beggining_test_code(dlist)
    # insert_at_end_test_code(dlist)
    # insert_at_given_position_test_code(dlist)
    # delete_at_beginning_end_test_code(dlist)
    # delete_at_position_test_code(dlist)
    # print_all_nodes_test_code(dlist)
    serach_key_test_code(dlist)