#builtin function to multiply all the numbers in a list
list = [4, 7, 8]
def multiplyList(list):
    result = 1
    for x in list:
        result = result * x
    return result

print (multiplyList(list))

import math
list2 = [7, 13, 3]
result = math.prod(list2)
print (result)
    
#builtin function that accepts a string and calculate the number of upper case letters and lower case letters
str = "ThereIsAProgrammingClass"
def string_test(s):
    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"] += 1
        elif c.islower():
            d["LOWER_CASE"] += 1
        else:
            pass
    return d
print(string_test(str))

#builtin function that checks whether a passed string is palindrome or not
def isPalindrome(s):
    rev = ''.join(reversed(s))
    if (s == rev):
        return True
    return False
 
word = input("Check for palindrome ")
print(isPalindrome(word))

#invoke square root function after specific milliseconds.
import math
seconds = 25100
milliseconds = 2123
x = seconds + milliseconds/1000
print("Square root of 25100 after 2123 milliseconds is ")
print (math.sqrt(x))

#Write a Python program with builtin function that returns True if all elements of the tuple are true
tuple1 = ("apple", "banana", "cherry")
result = all(tuple1)
print(result)