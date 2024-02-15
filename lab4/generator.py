#sqaures of numbers up to some number N
n = int(input("Enter number "))
i = 1
while i<=n:
  print (i*i)
  i+=1

#even numbers between 0 and n
n = int(input("Enter number "))
i = 0
list = []
while i<=n:
  if i%2==0:
    s = str(i)
    list.append(s)
  i+=1
result = ','.join(list)
print(result)

#numbers divisible by 3 and 4
n = int(input("Enter number "))
divBy12 = [i for i in range(0, n) if (i % 12 == 0)]
print(divBy12)

def division(n):
    for i in range(n):
        if i % 4 == 0 & i%3==0:
            value = True
        else:
            value = False
        print(i, value)

division(n)

#squares 
n = int(input("Enter number "))
i = 1
while i<n:
  print (i*i)
  i+=1

a = (i*i for i in range (1, n))
for i in a:
   print(i)

#a generator that returns numbers from n to 0
n = int(input("enter name "))
a = (n-i for i in range (0, n+1))
for i in a:
   print(i)
