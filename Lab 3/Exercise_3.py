

import glob
import math
import random

import time

# glob: List all Python files in the current directory
python_files = glob.glob("*.py")
print("Python files in the current directory:", python_files)

# math: Mathematical operations
print("Pi:", math.pi)
print("Square root of 16:", math.sqrt(16))
print("Factorial of 5:", math.factorial(5))

# random: Generate random number and select random item
random_number = random.randint(1, 10)
print("Random number between 1 and 10:", random_number)
items = ['apple', 'banana', 'cherry']
random_item = random.choice(items)
print("Randomly selected item:", random_item)

# help: Display help about math module
help(math.sqrt)

# time: Time-related functions
current_time = time.time()
print("Current time (in seconds since epoch):", current_time)
print("Sleeping for 2 seconds...")
time.sleep(2)
print("Awoke from sleep!")
local_time = time.ctime()
print("Local time:", local_time)
