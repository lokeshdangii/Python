'''
tell():

We can use tell() method to return current position of the cursor(file pointer).
The position(index) of first character in files is zero just like string index.
'''

f = open('abcde.txt','r')
print('Cursor position: ',f.tell())

print(f.read(5))
print('Cursor position: ',f.tell())

print(f.read(7))
print('Cursor position: ',f.tell())

print(f.readline())
print('Cursor position: ',f.tell())

print(f.read())
print('Cursor position: ',f.tell())

