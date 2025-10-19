"""
===========================================================
📘 PYTHON COLLECTIONS MODULE - COMPLETE EXPLAIN + EXAMPLES
Author : Veeresh H.
Purpose: Understand and Master all data structures from collections
===========================================================
"""

# ------------------------------------------------------------
# 1️⃣ COUNTER
# ------------------------------------------------------------
from collections import Counter

print("\n🔹 1. COUNTER – Count hashable objects")

nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
count = Counter(nums)

print("List:", nums)
print("Counter:", count)
print("Most Common:", count.most_common(2))   # Top 2 frequent numbers
print("Count of 3:", count[3])
print("Count of 99 (missing key):", count[99])  # Returns 0 safely
print("All Keys:", list(count.keys()))
print("All Values:", list(count.values()))

# ------------------------------------------------------------
# 2️⃣ DEFAULTDICT
# ------------------------------------------------------------
from collections import defaultdict

print("\n🔹 2. DEFAULTDICT – Auto-create missing keys with default value")

# Example 1: Default int counter
marks = defaultdict(int)
marks["Alice"] += 10
marks["Bob"] += 5
print("Marks Dictionary:", dict(marks))

# Example 2: Grouping using list as default
students = [('A', 'John'), ('B', 'Sam'), ('A', 'Anna')]
groups = defaultdict(list)
for section, name in students:
    groups[section].append(name)

print("Grouped Students:", dict(groups))

# ------------------------------------------------------------
# 3️⃣ DEQUE
# ------------------------------------------------------------
from collections import deque

print("\n🔹 3. DEQUE – Double-ended queue (fast append/pop both sides)")

dq = deque([1, 2, 3])
dq.append(4)       # add to right
dq.appendleft(0)   # add to left
print("Deque after append:", dq)

dq.pop()           # remove from right
dq.popleft()       # remove from left
print("Deque after pop:", dq)

# Real use case: queue operations
queue = deque()
queue.append("task1")
queue.append("task2")
print("Queue:", queue)
queue.popleft()  # process first task
print("Queue after processing:", queue)

# ------------------------------------------------------------
# 4️⃣ NAMEDTUPLE
# ------------------------------------------------------------
from collections import namedtuple

print("\n🔹 4. NAMEDTUPLE – Tuple with named fields (like lightweight class)")

Point = namedtuple('Point', ['x', 'y'])
p1 = Point(10, 20)
print("Point:", p1)
print("x =", p1.x, "y =", p1.y)

# Real example: Employee record
Employee = namedtuple('Employee', 'name id salary')
emp = Employee('Veeresh', 101, 55000)
print("Employee:", emp)
print("Name:", emp.name, "Salary:", emp.salary)

# ------------------------------------------------------------
# 5️⃣ ORDEREDDICT
# ------------------------------------------------------------
from collections import OrderedDict

print("\n🔹 5. ORDEREDDICT – Dictionary that remembers insertion order")

od = OrderedDict()
od['a'] = 10
od['b'] = 20
od['c'] = 30

print("OrderedDict:", od)

# Move a key to end or beginning
od.move_to_end('a')       # Move 'a' to end
print("After move_to_end('a'):", od)
od.move_to_end('b', last=False)  # Move 'b' to start
print("After move_to_end('b', last=False):", od)

# ------------------------------------------------------------
# 6️⃣ CHAINMAP
# ------------------------------------------------------------
from collections import ChainMap

print("\n🔹 6. CHAINMAP – Combine multiple dictionaries logically")

defaults = {'theme': 'dark', 'language': 'en'}
user = {'language': 'fr'}
admin = {'theme': 'light'}

settings = ChainMap(user, admin, defaults)
print("Combined Settings:", settings.maps)
print("Theme:", settings['theme'])
print("Language:", settings['language'])

# Update affects the first map only (user)
settings['language'] = 'es'
print("After change:", settings.maps)

# ------------------------------------------------------------
# ✅ END OF FILE
# ------------------------------------------------------------
print("\n🎯 Summary:")
print("""
Counter     → Count items quickly (frequency map)
defaultdict → Auto default values (no KeyError)
deque       → Fast queue/stack operations
namedtuple  → Named data structure like small class
OrderedDict → Dict that remembers insertion order
ChainMap    → Combine multiple dicts for layered configs
""")
