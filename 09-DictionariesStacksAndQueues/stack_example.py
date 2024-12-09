import queue

"""
A stack is a linear data structure that follows
the Last In, First Out (LIFO) principle.
This means the last element added to the stack
is the first one to be removed.
"""

# Create a stack
stack = queue.LifoQueue()

# Add numbers to the stack
stack.put(2)
stack.put(3)
stack.put(7)
stack.put(4)
stack.put(1)
stack.put(9)
stack.put(8)

# Print the stack size
print("Number of stack elements:", stack.qsize())

# Sum the last two numbers from the stack
last = stack.get()  # Get the top element
second_last = stack.get()  # Get the second-to-top element
print("Sum of the last two numbers:", last + second_last)

# Calculate the sum of the remaining elements in the stack
remaining_sum = 0
while not stack.empty():
    remaining_sum += stack.get()

print("Sum of the remaining stack elements:", remaining_sum)
