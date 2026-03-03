x = 10 # global

def test_scope():
    y = 20 # local
    print("Inside test_scope function...")
    
    print(f"x id is: {id(x)}")
    print(f"y id is: {id(y)}")
    
test_scope()

print("Outside the test_scope function...")
print(f"x id is: {id(x)}")


# --------------------------------
# OUTPUT
#---------------------------------
'''
Inside test_scope function...
x id is: 140732208200408
y id is: 140732208200728
Outside the test_scope function...
x id is: 140732208200408
'''
# Tasks:

# Explain why y is not accessible outside.
# Confirm whether x refers to same object inside and outside.

# -> OBSERVATIONS <-
# y is not accessible outside because it is a local variable and its scope is limited to the function test_scope. Once the function finishes exection, the local variable y is destroyed and cannot be accessed outside of the test_scope function.
# x is defined as a global variable and it can be accessed both inside and outside the function. The id of x is the same both inside and outside the function, which confirms that x refers to the same object in both cases.