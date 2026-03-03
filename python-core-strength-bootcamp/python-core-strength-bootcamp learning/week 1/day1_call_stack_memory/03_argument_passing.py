def modify_number(num):
    print(f"Inside the function, before modification: {num} and its id is {id(num)}")
    num += 10
    print(f"Still inside the function, after modification: {num} and its id is {id(num)}")
    
    
number = 5
print(f"Before calling the modify_number function: {number} and its id is {id(number)}")
modify_number(number)


# --------------------------
# OUTPUT:
# --------------------------
# Before calling the modify_number function: 5 and its id is 140732208200408
# Inside the function, before modification: 5 and its id is 140732208200408
# Still inside the function, after modification: 15 and its id is 140732208201688


# Now compare with:

def modify_list(lst):
    print("Inside before:", lst, id(lst))
    lst.append(99)
    print("Inside after:", lst, id(lst))

my_list = [1, 2, 3]
print("Outside before:", my_list, id(my_list))
modify_list(my_list)
print("Outside after:", my_list, id(my_list))


# Tasks:

'''
Explain why integer ID changes inside function.

Explain why list ID does not change.

Write explanation in your own words.

If you can’t explain it simply, you don’t understand it yet.
'''

# EXPLANATION:
# In Python, integers are immutable, which means that when we modify an integer (like adding 10), a new integer object is created in memory. 
# This is why the ID of the integer changes after modification. On the other hand, lists are mutable, which means that when we modify a list (like appending an element), we are modifying the same object in memory. 
# Therefore, the ID of the list remains the same before anf after modification.