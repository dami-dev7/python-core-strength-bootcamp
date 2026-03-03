def function_c():
    print("Inside function c.")
    

def function_b():
    print("Entering function b.")
    function_c()
    print("Exiting function b.")
    
def function_a():
    print("Entering function a.")
    function_b()
    print("Exiting function a.")
    
function_a()

# --------------------------------
# OUTPUT
#---------------------------------
'''
Entering function a.
Entering function b.
Inside function c.
Exiting function b.
Exiting function a.
'''
# Task:

# - Draw the call stack manually while this runs.

# - Identify when each frame is pushed and popped.

# -> OBSERVATIONS <-
# Function a is first called and it's stack frame created
# Then when dunction b is called, similarly a new stack frame us created for it
# Then also function c is called and it's stack frame is also created
# Then the stack frame of fucntion c gets removed 
# Then the stack frame of fucntion b gets removed 
# Then the stack frame of fucntion a gets removed 