text = input("Enter some text: ")

# Finding shortest word
shortest = min(text.split(), key=len)

# Displaying shortest word
print("Shortest word is: ", shortest)
print("And its length is: ", len(shortest))