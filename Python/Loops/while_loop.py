# What is a while loop?
# A while loop is a control flow statement that repeats a block of code as long as a given condition is True.

# It’s useful when you don’t know how many times you need to loop in advance.

# syntax
"""
while condition:
    # code to execute
"""


count = 0  # Step 1: Initialize a variable 'count' with 0
while count <= 10:  # Step 2: Check condition → Is count ≤ 10?
    print(count)  # Step 3: If condition is True → print the current value of count
    count = count + 1  # Step 4: Increase count by 1 (count = count + 1)
# Step 5: Go back to Step 2 and check again, until condition becomes False
