# Here are all major types of conditional statements in Python with examples:

# 1. Simple if Statement
# Executes a block only if the condition is True.
x = 5
if x > 0:
    print("Positive number")  # output: Positive number


# 2. if-else Statement
# Executes one block if True, otherwise another.
x = -3
if x > 0:
    print("Positive number")
else:
    print("Non-positive number")

# output: Non-positive number

# 3. if-elif-else (Multiple Conditions)
# Checks multiple conditions in sequence.
x = 0
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

# output: Zero


# 4. Nested if
# if inside another if.
x = 7
if x > 0:
    if x < 10:
        print("Single-digit positive number")

# output : Single-digit positive number


# 5. Conditional Expression (Ternary Operator)
# Short-hand for if-else in one line.
x = -2
msg = "Positive" if x > 0 else "Non-positive"
print(msg)

# output: Non-positive


# 6. match-case (Python 3.10+)
# Like switch in other languages, for pattern matching.
day = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Other day")

# output: Wednesday
