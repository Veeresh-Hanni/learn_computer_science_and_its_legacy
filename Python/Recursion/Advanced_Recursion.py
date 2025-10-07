def  number_recursive(num):

    # Termination Block
    if num == 0:
        return
    
    # Logic 
    print("Before Recursive Call: ",num)
    # num = num - 1

    # Recursive call
    number_recursive(num - 1)

    # This line executes after recursion popped  from stack
    print("After Recursive Call: ",num)

def factorial(num):
    if num == 0  or num == 1:
        return 1
    
    return num * factorial(num - 1)

def fibonacci(num):
    # print(f"Recursive Function invoked with number = {num}")
    if num <= 1:
        return num

    print("FIRST recursive call invoked")
    result1 = fibonacci(num - 1)
    print(f"Result1 value = {result1}")

    print("SECOND recursive call invoked")
    result2 = fibonacci(num - 2)
    print(f"Result2 value = {result2}")

    answer = result1 + result2
    print(f"Answer value = {answer}")

    return answer

    # return fibonacci(num - 1) + fibonacci(num - 2)

if __name__ == "__main__":
    # number_recursive(5)
    # print(factorial(5))
    print(fibonacci(10))