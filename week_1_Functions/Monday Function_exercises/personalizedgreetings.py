#Write a program that asks for a person's name and displays a personalized greeting using a function



user_name = input("enter your full name : ")

def greetings():
    print(f"hello, {user_name} welcome to our python reading study session")

greetings()   


#NOTE
#hoose a function with a parameter because it makes the function reusable
#  and independent of global variables. The same function can work with different
#  inputs every time it is called, making the code more flexible, easier to maintain, 
# easier to test, and less prone to unexpected side effects