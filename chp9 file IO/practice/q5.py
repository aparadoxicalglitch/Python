words = ["donkey", "kaddu", "mote"]

with open("sample.txt") as f:
    content = f.read()  # reads the txt file 


for word in words:  # checks if these words are present there or not 
    content = content.replace(word, "$%^@$^#") # replaces the word 
    with open("sample.txt", "w") as f:  # opens the sample.txt fie 
        f.write(content)  # writes the replaced words there 