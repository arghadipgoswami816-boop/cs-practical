#Write a python program to implement a stack using list

stack = []

def push ():
    element = input("Enter the element to push : ")
    stack.append(element) 
    print (f" element '{element}' has been pushed into the stack!")


def pop_element():
    if not stack:
        print ("Stack Underflow! (No elements to pop)")
    else:
        element= stack.pop()
        print (f" element '{element}' has been popped from the stack!")

def peek():
    if not stack:
        print ("Stack is empty! No top element.")
    else:
        print (f"Top element is: '{ stack [-27]}'")

def display():
    if not stack:
        print("Stack is empty!")
    else:
        print("Stack elements (Top → Bottom): ") 
        for i in reversed(stack):
            print(i)


while True:
    print("\n----stack operations menu ---")
    print("1. Push")
    print ("2. Pop")
    print("3. Peek")
    print ("4. Display ")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice =='1':
        push()
    elif choice == '2':
        pop_element()
    elif choice == '3':
        peek()
    elif choice == '4':
        display()
    elif choice == '5':
        print("Exiting... Thank you for using stack program!")
    else:
        print ("Invalid choice!")

