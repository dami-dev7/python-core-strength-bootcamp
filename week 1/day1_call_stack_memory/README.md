# Day 1 – Python Call Stack & Memory

## Objectives

- Understand how function calls create stack frames
- Distinguish local and global scope
- Understand argument passing (reference model)
- Understand stack vs heap memory
- Explore reference counting
- Explore garbage collection
- Analyze recursion and object identity using id()

---

## Concepts Covered

### 1. Stack Frames
Each function call creates a new stack frame containing:
- Local variables
- Function arguments
- Execution state

Stack frames are destroyed when the function returns.

---

### 2. Stack vs Heap

Stack:
- Stores function calls
- Stores local variable references
- Automatically cleaned after function returns

Heap:
- Stores actual Python objects (lists, dicts, instances)
- Managed by reference counting and garbage collector

---

### 3. Argument Passing

Python passes references to objects.
Mutable objects can be modified inside functions.
Immutable objects cannot be modified in-place.

---

### 4. Reference Counting

Objects are deleted when reference count reaches zero.

---

### 5. Garbage Collection

Handles circular references not resolved by reference counting.

---


🧠 Deep Understanding Questions (Write Answers in README)

What exactly lives in a stack frame?

Where do Python objects live?

Why can mutable objects cause side effects?

Why is recursion memory-expensive?

Why must you understand this before writing Flask apps?



## Reflection

(Write 2–3 sentences here after finishing the day)
Understanding the call stack and memory management in Python is crucial for writing efficient and bug-free code. It helps us grasp how functions execute, how variables are stored, and how to avoid common pitfalls with mutable objects and recursion. This foundational knowledge will be essential in building more complex applications, including Flask apps, where performance and memory management become even more critical.