#Write a list comprehension that creates a list 
# containing the squares of only the odd numbers from 1 to 20.


odd =[number **2 for number in range(1, 20) if number %2 == 1]

print(odd)