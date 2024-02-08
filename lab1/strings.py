#assign string to a variable
a = "Hello"
print(a)


#multiline string with using three quotes or three single quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#arrays
a="Hello, World!"
print (a[1])

#looping in a string
for x in "banana":
    print(x)

#string length
a = "Hello, World!"
print (len(a))

#check string with keyword in
txt = "The best things in life are free!"
print("free" in txt)
#or use if statement
if "free" in txt:
  print("Yes, 'free' is present.")

#check if not with keyword not in
txt = "The best things in life are free!"
print("cheap" not in txt)

#slicing
b = "Hello, World!"
print(b[2:5]) #gets characters from position
print(b[:5]) #from starts to position5 
print(b[2:]) #from position 2 to the end
print(b[-5:-2]) #negative numbers to start from the end

#upper case
a = "Hello, World!"
print (a.upper())
#lowercase
print (a.lower())

#remove whitespace
a = " Hello, World! "
print (a.strip())


#replace
a = "Hello, World!"
print (a.replace("H", "J"))

#split
a = "Hello, World!"
print (a.split(",")) #returns two strings from between specified separator

#string concatenation
a = "Hello"
b = "World"
c = a+ b
print (c)
d = a + " " + b
print (d)


#format()
age = 28
txt = "My name is James, I am {}"
print (txt.format(age))
#example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

