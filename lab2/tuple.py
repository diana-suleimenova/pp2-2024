#create tuple
thistuple = ("apple", "banana", "cherry")
print (thistuple)

#length is len()
print (len(thistuple))

#tuple with one item needs a comma
thistuple = ("apple",)
print(thistuple)

#construct tuple with tuple()
thistuple = tuple(("apple", "banana", "cherry")) 
print(thistuple)

#access tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) #index starts with 0
print(thistuple[-1]) #negative to start from the end

#range of items
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
print(thistuple[:4]) #4th index is not included
print(thistuple[-4:-1])

#if statement to check existence
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#change tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#add items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(y)

#add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#remove items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)

#assigning value = unpacking
fruits = ("apple", "cherry", "orange")
(green, red, orange) = fruits
print (green)
print(red)
print(orange)

#using asterisks
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits #* assigns to the left items

print(green)
print(yellow)
print(red)

#loops with index 
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#while
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#join tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#multiplying tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)



