import gc

class Node:
    def __init__(self):
        self.ref = None
        
a = Node()
b = Node()

a.ref = b
b.ref = a

del a
del b

print("Garbage collector collected:", gc.collect())

# OUTPUT:

# Garbage collector collected: 2

'''
Tasks:

Why doesn’t reference counting free them immediately?

What problem does cyclic reference create?

What does gc.collect() return?
'''

# EXPLANATIONS:
# 1. Reference counting doesn't free them immediately because both objects a and b reference each other, creating a cycle. This means that even though we have deleted the references to a and b, they still reference each other, preventing their reference count from reaching zero.
# 2. Cyclic reference creates a problem because it can lead to memory leaks. If two or more objects reference each other, they will never be garbage collected, even if there are no external references to them. This can cause the program to consume more memory over tieme, potentially leading to performance issues or crashes.
# 3. The gc.collect() function returns the number of unreachable objects that were collected and freed by the garbage collector. In this case, it returns 2, indicating that both a and b were collected and freed from memory.
