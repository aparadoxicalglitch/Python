with open("log.txt") as f:
    content = f.read() # or we can write it here as f.read().lower()

if 'python' in content.lower(): # checks if python word is present there or not
    print("Yes python is present")
else:
    print("No python is not present")