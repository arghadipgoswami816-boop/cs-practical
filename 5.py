#5-Write a python program to implement a stack using list.

stack = []   # empty list to represent stack

# Function to push element into stack
def push():
    element = input("Enter the element to push: ")
    stack.append(element)
    print(f"Element '{element}' has been pushed into the stack!")

# Function to pop (remove) element from stack
def pop_element():
    if not stack:
        print("Stack Underflow! (No elements to pop)")
    else:
        element = stack.pop()
        print(f"Element '{element}' has been popped from the stack!")

# Function to peek (see top element)
def peek():
    if not stack:
        print("Stack is empty! No top element.")
    else:
        print(f"Top element is: '{stack[-1]}'")

# Function to display all elements of stack
def display():
    if not stack:
        print("Stack is empty!")
    else:
        print("Stack elements (Top → Bottom):")
        for i in reversed(stack):
            print(i)

# Main menu-driven program
while True:
    print("\n------ STACK OPERATIONS MENU ------")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        push()
    elif choice == '2':
        pop_element()
    elif choice == '3':
        peek()
    elif choice == '4':
        display()
    elif choice == '5':
        print("Exiting... Thank you for using Stack Program!")
        break
    else:
        print("Invalid choice! Please enter between 1 to 5.")
