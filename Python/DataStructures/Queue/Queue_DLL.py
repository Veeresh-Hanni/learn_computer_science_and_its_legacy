import time

# Queue using Doubly Linked List(DLL)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Queue:

    def __init__(self):
        self.count = 0
        self.rear= None
        self.front = None
    
    def Enqueue(self, data):

        new_node = Node(data)

        if self.rear is None and self.front is None:
            self.front = new_node
            self.rear = new_node
            self.count += 1
            return
        
        self.rear.next = new_node
        new_node.prev = self.rear
        self.rear = new_node

        self.count += 1
    
    def Dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None
        
        data = self.front.data
        self.front = self.front.next

        if self.front is None:  # queue became empty
            self.rear = None
        else:
            self.front.prev = None

        self.count -= 1
        return data
    
    def peekFront(self):
        if self.front == None:
            print("Queue is empty")
            return
        
        return self.front.data
    
    def peekRear(self):
        if self.rear == None:
            print("Queue is empty")
            return
        
        return self.rear.data
    
    def print_all_values(self):
        if self.front is None:
            print("Queue is empty")
            return None
        
        current_node = self.front
        while current_node is not None:
            print(f"{current_node.data}")
            current_node = current_node.next
    
    def print_values_reverse(self):
        if self.rear is None:
            print("Queue is empty")
            return None
        

        current_node = self.rear

        while current_node is not None:
            print(f"{current_node.data}")
            current_node = current_node.prev
    
    def get_count(self):

        print(f"There are {self.count} items in Queue ")
        return self.count
    
    def is_empty(self):
        return self.count == 0

    def __str__(self):
        if self.front is None:
            return "Queue is empty"
        
        values = []
        current = self.front
        while current:
            if current == self.front and current == self.rear:
                values.append(f"[Front/Rear:{current.data}]")
            elif current == self.front:
                values.append(f"[Front:{current.data}]")
            elif current == self.rear:
                values.append(f"[Rear:{current.data}]")
            else:
                values.append(str(current.data))
            current = current.next
        return " <- ".join(values)


def dequeue_everything(q: Queue, delay=0):
    if q.is_empty():
        print("Empty Queue")
        return
    
    while not q.is_empty(): # ✅ keep dequeuing until empty
        print(f"{q.Dequeue()}")
        # time.sleep(delay) 
    print("Queue is Empty now")
    

def queue_test_code(q: Queue):

    start_time = time.time()  # record start time

    # --- Queue operations ---
    q.Enqueue(10)
    q.Enqueue(20)
    q.Enqueue(30)
    q.Enqueue(40)

    print("Initial Queue:")
    print(q)

    print("\nQueue List (front -> rear):")
    q.print_all_values()
    print()
    q.get_count()

    print("\nReverse Queue List (rear -> front):")
    q.print_values_reverse()
    print()

    print("Peek Front:", q.peekFront())  # 10
    print("Peek Rear:", q.peekRear())    # 40

    print("\nDequeue one element:", q.Dequeue())  # 10
    q.get_count()
    print("Is empty?", q.is_empty())

    # Try peeking after one dequeue
    print("Peek Front:", q.peekFront())
    print("Peek Rear:", q.peekRear())

    # Dequeue everything with 1-second delay
    print("\nDequeuing all elements:")
    dequeue_everything(q)
    print(q)  # should show empty queue

    end_time = time.time()  # record end time
    elapsed_time = end_time - start_time
    print(f"\nProgram execution time: {elapsed_time:.3f} seconds")

if __name__ == "__main__":
    q= Queue()
    queue_test_code(q)