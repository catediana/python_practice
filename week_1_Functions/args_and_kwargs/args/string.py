#Write a function that accepts any number of strings and prints each string on a new line

def print_strings(*args):

    for string in (args):
        print(string)
    
print_strings( "catherine", "nanjala", "mukalo")
   

# we use a for loop to accsess every element in a tuple one by one