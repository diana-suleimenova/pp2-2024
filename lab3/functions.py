#creating function
def my_func():
    print ("Hello from a function")

    #calliing the function
my_func()


#arguments
def my_func(fname):
    print (fname + " Jones ")

my_func("Emily")
my_func("Sasha")
my_func("Will")

#numbers of arguments
def my_func(fname, lname):
    print (fname + " " + lname)

my_func("Emily", "Smith")

#arbitrary arguments
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#keyword arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#arbitrary keyword arguments, ** if you don't know the number of keyword arguments
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#default parameter
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#list as an argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#return statement
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#pass statement
def myfunction():
  pass #func cannot be empty

#positional only arguments, use , /
def my_function(x, /):
  print(x)

my_function(3)

#keyword only arguments, use *,
def my_function(*, x):
  print(x)

my_function(x = 3)

#recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)