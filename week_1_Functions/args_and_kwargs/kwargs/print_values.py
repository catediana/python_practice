#Write a function that accepts any number of keyword arguments and prints only the values.


def print_values(**kwargs):
    for value in kwargs.values():
        print(value)


print_values(
    username= "catediana",
    role= "software engineer",
    country = "Kenya",
    experience = "two years"
)        