content = True # it wil evaluate only when there is true value if there is blank then it won't 
i = 1
with open("log.txt") as f:
    while content:
        content = f.readline()  # reads the line
        if 'python' in content.lower():
            print(content)
            print(f"Yes python is present on line number {i}") 
        i+=1