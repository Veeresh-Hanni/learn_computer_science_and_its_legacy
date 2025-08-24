class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.count = 0
        self.top = None
    
    def push(self,data):
        new_node = Node(data)

        new_node.next = self.top
        self.top = new_node
        self.count += 1
        print(f"push the value to stack: {data}")
    
    def pop(self) -> int:
        # Stack is empty
        if self.top == None:
            print("Stack is empty can't perform pop operation")
            return -100
        
        data = self.top.data
        self.top = self.top.next
        self.count -= 1
        print(f"Popped item from stack: {data}")
        return data
    
    def peek(self) -> int:
        # Stack is empty
        if self.top == None:
            print("Stack is empty")
            return -100
        print(f"Top data: {self.top.data}")
        return self.top.data
    
    def get_count(self) -> int:
        print(f"there are {self.count} items in stack")
        return self.count
    
    def print_all_values(self):
        # Stack is empty
        if self.top == None:
            print("Stack is empty ")
            return
        
        print("Elements in Stack")
        current_node = self.top
        while current_node is not None:
            print(f" {current_node.data}")
            current_node = current_node.next

def Stack_test_code(stack: Stack):

    stack.pop()
    stack.get_count()
    stack.peek()
    stack.print_all_values()

    stack.push(1)

    
    stack.get_count()
    stack.peek()
    stack.print_all_values()
    stack.pop()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.print_all_values()

    stack.pop()

    stack.peek()
    stack.print_all_values()
    stack.get_count()

class Stack_List:
    def __init__(self):
        self.count = 0
        self.top = None
        self.stack = []

    def push(self, data):
        self.stack.append(data)
        self.top = data
        self.count += 1
    
    def pop(self):
        if not self.stack:
            print("Stack is Empty")
            return None

        popped = self.stack.pop()
        self.count -= 1
        self.top = self.stack[-1] if self.stack else None
        return popped
    
    def peek(self):
        if not self.stack:
            print("Stack is Empty")
            return None
        return self.top

    def display(self):
        if not self.stack:
            print("Stack is Empty")
            return
        print("Stack elements (bottom → top):", self.stack)


if __name__ == "__main__":

    # stack = Stack()
    # Stack_test_code(stack)
    s = Stack_List()
    s.push(10)
    s.push(20)
    s.push(30)

    s.display()     # Stack elements (bottom → top): [10, 20, 30]
    print("Peek:", s.peek())   # Peek: 30

    print("Popped:", s.pop())  # Popped: 30
    s.display()                # [10, 20]

    print("Peek:", s.peek())   # Peek: 20
