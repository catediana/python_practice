# Write a function that accepts any number of keyword arguments and prints 
# each key together with its corresponding value.

def display_profile(**kwargs):

    #printing the enrire dictionary
    print("dictionary content:", kwargs)

     #loopinf through the dictionary so as to access the key value pairs
    for key , value in kwargs.items():
        print (f"key:{key}, value:{value}")

display_profile(username='catediana', role='software engineer')   
    