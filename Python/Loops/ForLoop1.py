# -----------------------------
# RANGE AND BASIC FOR LOOPS
# -----------------------------
values = range(10)  # Creates a range of numbers from 0 to 9

for item in values:  # Iterates over the numbers in 'values'
    print(item)  # Prints each number from 0 to 9

# Using range with start, stop, step
for item in range(1, 10, 1):  # Start at 1, stop before 10, step by 1
    print(item)

# Looping in reverse using negative step
for item in range(10, 1, -1):  # Start at 10, go down to 2 (stop before 1)
    print(item)

# -----------------------------
# LOOPING OVER A LIST
# -----------------------------
students = ["Veeresh", "Basu", "Guru", "Siddarth"]

for student in students:
    print(student.lower())  # Convert each name to lowercase and print

# -----------------------------
# LOOPING OVER A SET
# -----------------------------
unique_numbers = {1, 2, 2, 3, 4, 4, 5}  # Sets automatically remove duplicates

for elements in unique_numbers:  # Iterates over unique elements only
    print(elements)

# -----------------------------
# LOOPING OVER A DICTIONARY
# -----------------------------
student_scores = {"Alice": 45, "Bob": 34, "Charlie": 23}

for student in student_scores:  # Iterates over keys (student names)
    print(f"{student} has {student_scores[student]}")  # Access value using key

# Better way: iterate over key-value pairs
for student, scores in student_scores.items():
    print(f"{student} has marks: {scores}")

# -----------------------------
# NESTED LOOPS: MULTIPLICATION TABLE
# -----------------------------
for i in range(2, 11):  # Outer loop for each number (2–10)
    print(f"\nMultiplication Table : {i}\n")
    for j in range(1, 11):  # Inner loop for multiplying with 1–10
        print(f"{i} X {j} = {i*j}")

# -----------------------------
# SEARCHING FOR A STUDENT IN A LIST
# -----------------------------
students = [
    "Aarav Sharma",
    "Ishita Verma",
    "Rahul Mehta",
    "Priya Singh",
    "Karan Patel",
    "Neha Reddy",
    "Aditya Iyer",
    "Sneha Nair",
    "Rohan Das",
    "Anjali Gupta",
    "Vikram Choudhary",
    "Simran Kaur",
    "Arjun Malhotra",
    "Pooja Joshi",
    "Siddharth Rao",
    "Meera Banerjee",
    "Harsh Vardhan",
    "Kavya Pillai",
    "Manish Sinha",
    "Ritika Bansal",
    "Yash Dubey",
    "Divya Jain",
    "Nikhil Kapoor",
    "Swati Mishra",
    "Abhishek Chauhan",
    "Shreya Saxena",
    "Gaurav Thakur",
    "Tanvi Deshmukh",
    "Rajat Bhargava",
    "Nisha Kulkarni",
    "Vivek Srivastava",
    "Aditi Agarwal",
    "Mohit Khanna",
    "Ankita Rawat",
    "Rohit Tiwari",
    "Pallavi Desai",
    "Saurabh Ghosh",
    "Ananya Menon",
    "Kunal Bhatia",
    "Rashmi Prasad",
    "Rashmi Prasad",  # Duplicate name for testing
]

std_name = input("Enter a student name: ")  # User enters name to search

found = False
for index, name in enumerate(students):  # Loop with index and value
    if name.lower() == std_name.lower():  # Compare ignoring case
        # Get next student if exists, else display "No next student"
        next_student = (
            students[index + 1]
            if index + 1 < len(students)
            else "No next student (last in list)"
        )
        print(f"{std_name} found at index {index} → Next student: {next_student}")
        found = True
        break  # Stop loop when found

if not found:
    print(f"{std_name} not found in the list")

# -----------------------------
# FINDING DUPLICATE NAMES (NESTED LOOPS)
# -----------------------------
duplicates = []


# for name in students:
#     if students.count(name) > 1 and name not in duplicates:
#         duplicates.append(name)

for i in range(len(students)):  # Outer loop from 0 → last
    for j in range(len(students) - 1, i, -1):  # Inner loop from last → i
        if students[i].lower() == students[j].lower():  # Case-insensitive
            if students[i] not in duplicates:  # Avoid adding duplicates twice
                duplicates.append(students[i])

if duplicates:
    print("Duplicate names found:")
    for name in duplicates:
        print(name)
else:
    print("No duplicate names found.")

# -----------------------------
# LIST COMPREHENSIONS
# -----------------------------
# Generate list of numbers from 1 to 10
number = [number for number in range(1, 10 + 1)]
print(number)

# Generate squares of numbers 1 to 10
squares = [number**2 for number in range(1, 10 + 1)]
print(squares)

# Generate squares of even numbers
even_squares = [number**2 for number in range(1, 10 + 1) if number & 1 == 0]
print(even_squares)

# Generate squares of odd numbers
odd_squares = [number**2 for number in range(1, 10 + 1) if number % 2 != 0]
print(odd_squares)
