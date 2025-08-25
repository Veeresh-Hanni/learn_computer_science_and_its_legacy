

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Queue:

    def __init__(self):
        self.rear = None
        self.front = None
        self.count = 0

    def Enqueue(self, data):
        # Insert from rear
        new_node = Node(data)
        #case 1: Queue is empty
        if self.rear is None:
            self.front = new_node
        else:
            # case 2: Queue has some nodes
            # current node next is rear
            self.rear.next = new_node

        self.rear = new_node
        self.count += 1
    
    def Dequeue(self) -> int:
        if (self.front == None):
            print("Queue is Empty")
            return
        
        # take a copy of front value
        return_data = self.front.data
        # move next node
        self.front = self.front.next

        # if there was only one elements , queue becomes empty
        if self.front == None:
            self.rear = None

        self.count -= 1
        print(f"Removed element: {return_data}")
        return return_data
    
    def peek(self):

        if self.front == None:
            print("Queue is Empty")
            return

        return self.front.data

    def get_count(self) -> int:
        return self.count
    
    def print_all_elements(self):
        if self.front == None:
            print("Queue is Empty")
            return
        
        current_node = self.front

        while current_node is not None:
            print(f"{current_node.data} --> ",end=" ")
            current_node = current_node.next
        print()

if __name__ == "__main__":
    queue = Queue()

    queue.Dequeue()
    queue.print_all_elements()
    queue.get_count()

    queue.Enqueue(1)
    queue.print_all_elements()
    queue.get_count()

    queue.Dequeue()
    queue.print_all_elements()

    queue.Enqueue(1)
    queue.Enqueue(2)
    queue.Enqueue(3)
    queue.Enqueue(4)
    queue.Enqueue(5)
    queue.print_all_elements()
    queue.get_count()
    
    value = queue.Dequeue()
    print(f"Removed value {value} from Queue")
    queue.print_all_elements()