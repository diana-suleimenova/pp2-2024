#create a set
set1 = {"apple", "banana", "cherry", "banana"}
print (set1) #unordered
#duplicates will be ignored
#true and 1 are considered the same
#as well as false and 0

#length of set
print(len(set1))

#set constructor
thisset = set(("apple", "banana", "cherry"))
print(thisset)

#access items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#checking existence
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#add new item
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#add items from another set
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)

#update() does not need set, can be other iterable object
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print(thisset)

#remove item
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset) #if item does not exist there will be error

#but with discard there will not be
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#pop() also removes item, but it's random
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#clear() empties the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#del deletes the while set
thisset = {"apple", "banana", "cherry"}
del thisset
#print(thisset)

#join sets with union()
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#or join with update()
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#keep only items that exist in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

#everything but not the duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

