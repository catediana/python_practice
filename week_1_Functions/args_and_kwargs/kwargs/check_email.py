#Write a function that accepts any number
#  of keyword arguments and checks whether the key "email" exists.

def check_email(**kwargs):
    
        if "email" in kwargs:
            print(f"found email: {kwargs['email']}")
        else:
            print("please check again")   



check_email(
    username= "catediana",
    role= "software engineer",
    country = "Kenya",
    experience = "two years",
    email = "catherine nanyala@gmail.com"
)        