
#Write a function that accepts a student's score and returns the corresponding letter grade.
def letter_grade(score):
    if score >= 80:
        return "A"
    elif score >= 60:
        return "B"
    else:
        return"C"
print(letter_grade(150))   