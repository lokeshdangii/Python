text = input("Enter some text: ")

# Finding longest word
shortest = min(text.split(), key=len)

# Displaying longest word
print("Shortest word is: ", shortest)
print("And its length is: ", len(shortest))