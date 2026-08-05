# Write a function that accepts any number of keyword arguments and returns the total 
# number of keyword arguments that were passed to the function.


def count_kwargs (**kwargs):
    #for key , value in kwargs.items():
        return len(kwargs)


print(count_kwargs(
    username= "catediana",
    role= "software engineer",
    country = "Kenya",
    experience = "two years"
) )       