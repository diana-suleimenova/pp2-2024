#Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
import os
print('Exist:', os.access('c:\\Users\\Public\\C programming library.docx', os.F_OK))
print('Readable:', os.access('c:\\Users\\Public\\C programming library.docx', os.R_OK))
print('Writable:', os.access('c:\\Users\\Public\\C programming library.docx', os.W_OK))
print('Executable:', os.access('c:\\Users\\Public\\C programming library.docx', os.X_OK))

#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os
print("Test a path exists or not:")
path = r'g:\\testpath\\a.txt'
print(os.path.exists(path))
path = r'g:\\testpath\\p.txt'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))

#Write a Python program to count the number of lines in a text file. 
with open(r'/Users/dianasuleimenova/Desktop/row.txt', 'r') as fp:
    lines = len(fp.readlines())
    print('Total Number of lines:', lines)

#Write a Python program to write a list to a file.
items = ['Mango', 'Orange', 'Apple', 'Lemon']
file = open('items.txt','w')
for the a in items:
	file.write(a+"\n")
file.close()

#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import string, os
if not os.path.exists("letters"):
   os.makedirs("letters")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)

#Write a Python program to copy the contents of a file to another file
with open('/Users/dianasuleimenova/Desktop/row.txt','r') as firstfile, open('second.txt','a') as secondfile: 
    for line in firstfile: 
             secondfile.write(line)

#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

#Write a Python program to list only directories, files and all directories, files in a specified path
import os
path = 'g:\\testpath\\'
print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nOnly files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nAll directories and files :")
print([ name for name in os.listdir(path)])



