class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:

    def __init__(self):
        self.tail = None

    # This function insert a node after tail (start)
    # If there is node at start then it becomes the 2nd node
    # Time Complexity is O(1)
    def insert_at_beginning(self,data):
        new_node = Node(data)
        # Empty List
        if (self.tail == None):
            self.tail = new_node
            new_node.next = new_node
            return

        # Single node and  Multi Node
        new_node.next = self.tail.next
        self.tail.next = new_node

    # Time Complexity is O(1)
    def insert_at_end_tail(self, data):
        new_node = Node(data)
        # case 1: Empty List
        if (self.tail == None):
            self.tail = new_node
            new_node.next = new_node
            return
        
        # case 2: single node and Multi Node
        new_node.next = self.tail.next
        self.tail.next = new_node
        self.tail = new_node

    def delete_at_beginning(self):

        if (self.tail == None):
            print("List is Empty")
            return
        
        # case 1: if single node list will empty
        if (self.tail.next == self.tail):
            self.tail = None
            return
        
        # case 2: two or More Nodes
        self.tail.next = self.tail.next.next

    # Node before tail becomes te new tail
    # since we don't have address of node before tail node
    # we have to traverse to each there
    def delete_at_end_tail(self):
        # Empty List
        if(self.tail == None):
            return
        
        # case 2: single node
        if self.tail.next == self.tail:
            self.tail = None
            return
        
        # case 3: two or more nodes
        # find the reference to the previous to the tail node
        new_tail = self.tail.next
        while (new_tail.next != self.tail):
            new_tail = new_tail.next
        
        new_tail.next =self.tail.next
        self.tail = new_tail

    def print_all_nodes(self):
        # case 1: List is empty
        if (self.tail == None):
            print("List is Empty")
            return
        
        current_node = self.tail.next
        while (True):
            print(f"{current_node.data} --> ", end=" ")

            if (current_node == self.tail):
                break
            
            current_node = current_node.next
        
        print(f"Tail ({current_node.data}) point to first node data ({self.tail.next.data})")
    
    def search_key(self, key):
        # case 1: List is empty
        if (self.tail == None):
            print("List is Empty")
            return
        
        current_node = self.tail.next
        while (True):

            if (current_node.data == key):
                print(f"{key} is found in list ✅")
                return
            
            if current_node == self.tail:
                break

            current_node= current_node.next
        
        print(f"{key} is not present in list ❌")



def Circular_Linked_List_tests(clist: CircularLinkedList):
    # List is emptyand trying to delete a node
    clist.delete_at_beginning()
    clist.delete_at_end_tail()
    clist.print_all_nodes()
    clist.search_key(40)

    # perform insert and delete single node
    clist.insert_at_beginning(40)
    clist.delete_at_beginning()
    clist.print_all_nodes()
    clist.search_key(40)

    # perform insert at tail and delete at tail 
    clist.insert_at_end_tail(50)
    clist.delete_at_end_tail()

    # create list with multiple node
    clist.insert_at_beginning(10)
    clist.print_all_nodes()
    clist.search_key(40)

    clist.insert_at_beginning(20)
    clist.insert_at_beginning(30)

    clist. insert_at_end_tail(40)

    clist.print_all_nodes()
    clist.search_key(40)
    clist.search_key(100)

class Infine_loop_demo(CircularLinkedList):

    def inserts_test(clist: CircularLinkedList):
        clist.insert_at_beginning(10)
        clist.insert_at_beginning(20)
        clist.insert_at_beginning(30)
        clist.insert_at_beginning(40)
    
    def search_key(self, key):
        # case 1: List is empty
        if (self.tail == None):
            print("List is Empty")
            return
        
        current_node = self.tail.next
        while (True):

            if (current_node.data == key):
                print(f"{key} is found in list ✅")
                # return
                break
            
            # Must add break statements to avoid Infinite loop
            # if current_node == self.tail:
            #     break

            current_node= current_node.next
        
        print("Key is not present in list ❌")

def infinite_loop_demo(infy_loop: Infine_loop_demo):
    infy_loop.inserts_test()
    infy_loop.search_key(100)


if __name__ == "__main__":
    clist = CircularLinkedList()
    Circular_Linked_List_tests(clist)
    # infinite_loop_demo(Infine_loop_demo())