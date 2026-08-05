#Write a function that accepts any number of keyword arguments and prints only the keys.

def print_keys(**kwargs):
    for key in kwargs:
        print(f"key :{key}")

print_keys(
     username= "catediana",
     role= "software engineer",
     country = "Kenya",
     experience = "two years"
)        
        
