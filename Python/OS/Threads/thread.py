import threading
import time

def task(name):
    print(f"Thread {name} starting...")
    time.sleep(2)
    print(f"Thread {name} finished!")

# Create two threads
t1 = threading.Thread(target=task, args=("A",))
t2 = threading.Thread(target=task, args=("B",))

t1.start()
t2.start()

t1.join()
t2.join()

print("All threads completed!")