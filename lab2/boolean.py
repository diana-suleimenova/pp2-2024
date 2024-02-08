#compare two values
print (10<9)
print (9==9)
print (12>4)

#if statement
a = 54
b = 25
if (b>a):
  print ("b is greater than a")
else:
  print ("b is not greater than a")


#bool() function 
print(bool("Hello"))
print(bool(62))

#bool() function another method
x = "Hello"
y = 4

print(bool(x))
print(bool(y))

#checking if they have value
bool("abc")
bool(65)
bool(["apple", "cherry", "banana"])

#checking what evaluates to false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#_len_ function that evaluates to false
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#returning a boolean value
def myFunction() :
  return True

print(myFunction())

#returning a boolean value example
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

  #isinstance(), shows if an object is of certain data type
  x = 1000
print(isinstance(x, int))