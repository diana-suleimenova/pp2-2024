#create a list
list = ["cherry", "apple", "banana", "orange"]
print (list)
#the first item has index 0

#list length
print(len(list))

#a list can have different data types
list1 = ["abc", 34, True, 40, "male"]

#type of list
list = ["cherry", "apple", "banana", "orange"]
print (type(list))

#construct a list with list()
#thislist = list(("apple", "banana", "cherry"))
#print (thislist)
#access items
thislist = ["cherry", "apple", "banana", "orange"]
print (thislist[1])
print(thislist[-1])

#range of indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#change item value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#change a range of items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#insert a value
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#append items (add an item to the end)
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#extend list by adding items from another list
thislist = ["apple", "banana", "cherry"]
fruits = ["mango", "pineapple", "papaya"]
thislist.extend(fruits)
print(thislist)

#extend() adds items from not only lists, but also tuples, sets, etc
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#remove the item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#pop() removes the specific item
thislist = ["apple", "banana", "cherry"]
thislist.pop(0)
print(thislist)
#del also removes specific item
del thislist[0]
print(thislist)

#clear empties the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#loops
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#loops through the index
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#syntax
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

#sort - it is case sensitive, uppercase before lowercase
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist.sort()
print(thislist)

#descending
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist.sort(reverse = True)
print(thislist)

#customise function - how close they are to 50
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#reverse() regardless of alphabet
thislist = ["banana", "apple", "cherry"]
thislist.reverse()
print(thislist)

#copy list
thislist = ["banana", "apple", "cherry"]
newlist = thislist.copy()
print(newlist)

#join lists - method 1
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
#method 2
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

#method3
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)





