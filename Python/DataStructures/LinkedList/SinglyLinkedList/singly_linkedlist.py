# class which represents node in singlylinkedlist
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# class implements all the operation for singly linked list
class SinglyLinkedList:

    def __init__(self):
        self.head = None

    # this function add node at the beginning
    # This needs to handle two scenerios/ cases
    # 1) When list is empty
    # 2) List has some elements
    def insert_at_beginning(self,data):
        # create New node
        new_node = Node(data)

        # case 1: if the list is empty make new-node is head
        if self.head == None:
            self.head = new_node
            return
        
        # case 2: If the  list is not empty, make the new node as head and point to the old head
        new_node.next = self.head
        self.head = new_node
        return

    def delete_at_beginning(self):
        """
        Removes the first node in the list by updating head pointer.
        Handles empty and single-node list cases.
        """
        if self.head is None:
            return
        

        # two or more nodes present
        self.head = self.head.next

    def delete_at_end(self):
        # list is empty
        if self.head == None:
            return
        
        # list has one node
        if self.head.next == None:
            self.head = None
            return

        # two or more nodes in list
        current_node = self.head

        while(current_node.next.next != None):
            current_node = current_node.next

        current_node.next = None

    def insert_at_given_position(self, data, insert_position):
        # position invalid
        if insert_position <= 0:
            print("Invalid position")
            return
        
        # insert at first position

        if insert_position == 1:
            self.insert_at_beginning(data)
            return
        
        # insert at other position 2 or greater
        current_node = self.head
        
        current_position = 1

        while ( current_position < insert_position -1 and current_node is not None):
            current_position += 1
            current_node = current_node.next
        
        if current_node == None:
            # if want to add at end call insert_at_end method to addd node at end
            # self.insert_at_end()
            
            # otherwise throw error
            print("Invalid position reach last")
            # raise IndexError("Position out of range")
            return
        
        new_node = Node(data)

        new_node.next = current_node.next
        current_node.next = new_node
    
    def delete_at_given_position(self,delete_position):

        # position invalid
        if delete_position <= 0:
            print("Invalid position")
            return
        
        # insert at first position
        if delete_position == 1:
            self.delete_at_beginning()
            return
        
        # insert at other position 2 or greater
        current_node = self.head
        
        current_position = 1

        while ( current_position < delete_position -1 and current_node is not None):
            current_position += 1
            current_node = current_node.next
        
        if current_node == None:
            # if want to add at end call insert_at_end method to addd node at end
            # otherwise throw error
            print("Invalid position reach last")
            return
        
        
        current_node.next = current_node.next.next

    # print list nodes
    def print_nodes(self):
        # if list is empty
        if self.head == None:
            print("List is empty")
            return
        
        # not list empty
        current_node = self.head

        while current_node is not None:

            print(current_node.data, "->", end=" ")

            current_node = current_node.next

        print("None")

    # search any node in list
    def search(self, key):
        # if list is empty
        if self.head == None:
            print("List is empty")
            return
        
        # not list empty
        current_node = self.head
        while current_node is not None:

            if (key == current_node.data):
                
                print(f"{key} Found")
                return
            
            current_node = current_node.next

        print("not found")

# invocation code for insert/delete at_given_position 
def insert_delete_at_given_position(list: SinglyLinkedList):


    list.insert_at_given_position(data = 10, insert_position = -1)
    list.delete_at_given_position(delete_position = -1)

    list.insert_at_given_position(data = 10,insert_position = 1)
    list.delete_at_given_position(delete_position = 1)

    list.insert_at_given_position(data = 12, insert_position = 2)
    list.insert_at_given_position(data = 14, insert_position = 3)

    list.insert_at_given_position(data = 100, insert_position = 10)

    # list.delete_at_given_position(1)

# invocation code for delete at end beginning
def delete_opearations_start_end(list: SinglyLinkedList):
    list.delete_at_beginning()
    list.delete_at_end()

    list.insert_at_beginning(12)
    list.delete_at_beginning()

    list.insert_at_beginning(10)
    list.delete_at_end()

    list.insert_at_beginning(13)
    list.insert_at_beginning(24)
    list.insert_at_beginning(28)
    list.delete_at_end()
    list.delete_at_end()

def print_list_driver_code(list: SinglyLinkedList):
    list.print_nodes()
    list.insert_at_beginning(13)
    list.print_nodes()

    # list.insert_at_beginning(28)

    list.insert_at_given_position(23,2)
    list.print_nodes()

    list.insert_at_beginning(55)
    list.print_nodes()

def search_driver_code(list: SinglyLinkedList):

    list.search(23)
    list.search(5)
# driver code to test above class
if __name__ == "__main__":
    # create Singly Linked list

    list = SinglyLinkedList()

    # insert a element
    # list.insert_at_beginning(1)
    # slist.insert_at_beginning(34)

    # inserrt at given position
    # insert_delete_at_given_position(list)

    # print("List is Created successfully")

    # # print data
    # print("Head Node data is ", list.head.data)
    # print("Next node data is", list.head.next.data)
    # print("Next node data is", list.head.next.next.data)

    # delete_opearations_start_end(list)
    print_list_driver_code(list)
    search_driver_code(list)