#creating variables
x = 3
y = "Emily"
print(x)
print(y)

#casting - specifying the data type
x = str(2)
y = int(2)
z = float(2)

#get the data type
x = 4
y = "Emily"
print (type(x))
print (type(y))

#case sensitive 
a=4
A="James"
#A will not overwrite a

#assign many values in one line
x, y, z = "Orange", "Cherry", "Banana"
print(x)
print(y)
print(z)

#one value to multiple variables
x = y = z = "Banana"
print(x)
print(y)
print(z)

#collection
fruits = ["Orange", "Cherry", "Banana"]
x, y, z = fruits
print(x)
print(y)
print(z)

#output several variables
x = "Python"
y = "is"
z="awesome"
print (x, y, z)
#or use + but then they are not separated by space
print (x + y + z)

#for numbers + works as addition
x = 3
y=1
print (x+y)


#global variables
x = "awesome"
def func():
    print ("Python is "+x)

func()

#global keyword - variable created in a func is usually local
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

