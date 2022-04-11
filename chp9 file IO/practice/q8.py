with open("this.txt") as f:
    content = f.read() # opens and reads the file

with open("copy.txt", 'w') as f:
    f.write(content) # writes that content here 