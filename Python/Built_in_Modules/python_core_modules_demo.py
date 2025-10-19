import itertools, operator, math, statistics, random, datetime, os, sys, json, re, logging, threading, uuid
from collections import Counter, defaultdict, deque
from functools import reduce
from pathlib import Path

# 1️⃣ collections
nums = [1, 2, 2, 3, 3, 3]
print("Counter:", Counter(nums))
dd = defaultdict(int)
for n in nums: dd[n] += 1
print("defaultdict:", dict(dd))
dq = deque(nums)
dq.appendleft(0)
print("deque:", dq)

# 2️⃣ itertools
print("Combinations of 3 choose 2:", list(itertools.combinations([1,2,3], 2)))
print("Permutations of 'abc':", list(itertools.permutations('abc', 2)))

# 3️⃣ operator + reduce
nums = [1, 2, 3, 4]
print("Sum using reduce:", reduce(operator.add, nums))

# 4️⃣ math, statistics, random
print("sqrt(16):", math.sqrt(16))
print("Mean:", statistics.mean(nums))
print("Random choice:", random.choice(nums))

# 5️⃣ datetime
now = datetime.datetime.now()
print("Now:", now.strftime("%Y-%m-%d %H:%M:%S"))

# 6️⃣ os, pathlib
print("Current directory:", os.getcwd())
path = Path(".")
print("Files in dir:", [p.name for p in path.iterdir()])

# 7️⃣ json, re
data = {"name": "Veeresh", "lang": "Python"}
json_str = json.dumps(data)
print("JSON string:", json_str)
print("Regex match:", re.findall(r'\d+', "My age is 21 years"))

# 8️⃣ logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info log")

# 9️⃣ threading
def task():
    print("Running in thread")

t = threading.Thread(target=task)
t.start()
t.join()

# 🔟 uuid
print("Unique ID:", uuid.uuid4())

print("\n✅ Demo completed — explored many core modules!")
