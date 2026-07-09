#Write a function that returns the largest of three numbers
def largest_number(a ,b ,c):
    if a> b  and a> c:
        return a
    elif b > a and b > c :
       return b
    else:
        return c
    
           
print(largest_number(2 , 7, 9))