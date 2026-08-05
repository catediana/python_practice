#Write a function that accepts any number of numbers and returns the largest number.

def largest_number(*args):
    if not args:
        return None
# variable holding the largest number
    largest = args[0]
    for number in args:
        if number > largest:
            largest = number

    return largest


print(largest_number(12, 23, 4, 6, 9))    