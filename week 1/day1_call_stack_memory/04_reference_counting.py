import sys

a = [1, 2, 3]

print("Initial reference count of a :", sys.getrefcount(a))

b = a

print("Reference count after assigning b = a:", sys.getrefcount(a))

c = a

print("After assigning c to a:", sys.getrefcount(a))

b = None

print("Reference count after removing b:", sys.getrefcount(a))


# ---------------------
# TASKS
# ---------------------

'''
Tasks:

Why is refcount always +1 higher than expected?

When would this object be deleted?
'''

# OBSERVATIONS:
# 1. The reference count is always +1 higher than expected because the sys.getrefcount() function itself creates a temporary reference to the object when it is called.
   ## This means that when you call sys.getrefcount(a), it adds an additional reference to the object 'a' for the duration of the function call, which is why the count is always one more than the actual number of references in your code.
   
# 2. When the reference count of an object drops to zero, it means that there are no more references to that object in the program. At this point, the memory allocated for that object can be freed, and the object is effectively deleted from momory.
  ## In python, this process is handled by the garbage collector, which automatically manages memory.
  
  
  