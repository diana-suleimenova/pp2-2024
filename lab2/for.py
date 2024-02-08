#example for loops
fruits = ["cherry", "apple", "banana"]
for x in fruits:
    print (x)

#looping through a string
for x in "banana":
    print(x)

#break statement
fruits = ["cherry", "apple", "banana", "melon"]
for x in fruits:
    print (x)
    if x == "banana":
        break

#continue statement
fruits = ["cherry", "apple", "banana", "melon"]
for x in fruits:
    if x == "apple":
        continue
    print (x)

#range() function
for x in range(6):
  print(x)

#range() function starting with number other than 0
for x in range(2, 6):
  print(x)

#range() increasing by certain number
for x in range(3, 30, 4):
  print(x)

#else in for loop
for x in range(8):
  print(x)
else:
  print("Finally finished!")

#else in for loop example
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

  #nested loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#pass statement
for x in [0, 1, 2]:
  pass