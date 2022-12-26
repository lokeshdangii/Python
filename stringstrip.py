var1 = input("Enter value:")
word_list = []
temp_word = ""
for i in range(len(var1)):
    if var1[i] == " ":
        word_list.append(temp_word)
        temp_word=" "
    else:
        temp_word = temp_word+var1[i]

word_list.append(temp_word)
print("user defined sentence:",var1)
print("Word List:",word_list)