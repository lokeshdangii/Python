data='I am a good boy with bad attiquetes.'
f=open('abc.txt','w')
f.write(data)
f.close()

with open('abc.txt','r+') as f:
    text = f.read()
    print(text)
    print('Cursor position: ',f.tell())

    print('Cursor position: ',f.tell())
    f.seek(12)
    print('Cursor position: ',f.tell())

    # f.write('boy with good attiquetes.')
    # f.seek(0)
    # print(f.read())
    # f.seek(0)
    # text=f.read()
    # print('Data with modification: ',text)
    # print('Cursor position: ',f.tell())
    # f.seek(0)
    # print('Cursor position: ',f.tell())

    f.write("man not")
    f.seek(0)
    print(f.read())

