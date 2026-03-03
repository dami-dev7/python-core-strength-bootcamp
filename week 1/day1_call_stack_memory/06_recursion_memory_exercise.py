def recursive_function(n):
    x = [n]
    print(f"Entering n={n}, id(x)={id(x)}")

    if n > 0:
        recursive_function(n - 1)

    print(f"Exiting n={n}, id(x)={id(x)}")

recursive_function(3)


# ------------------------
# OUTPUT:
# -----------------------

# Entering n=3, id(x)=2065920350464
# Entering n=2, id(x)=2065920348544
# Entering n=1, id(x)=2065923976768
# Entering n=0, id(x)=2065920686976
# Exiting n=0, id(x)=2065920686976 
# Exiting n=1, id(x)=2065923976768 
# Exiting n=2, id(x)=2065920348544 
# Exiting n=3, id(x)=2065920350464 


'''
Required Analysis:

Does each call create a new x?

Why are IDs different?

When is each list destroyed?

At what moment is the stack frame removed?
'''

# OBSERVATIONS:
# 1. Yes, each call creates a new list x. This is evident from the different IDs printed for each call.
# 2. The IDs are different because each recursive call creates a new local variable `x`, which is a new list object in memory. Even though the variable name is the same, they are distinct objects with different memory addresses.
# 3. Each list 'x' is destroyed when the function call that created it finishes execeution and the stack frame is removed. This happens after the print statement that indicates exiting the function for each value of n.
# 4. The stack frame for each call is removed after the function finishes executing.