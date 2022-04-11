with open('another.txt', 'r') as f:
    a = f.read()
with open('another.txt', 'w') as f:
     a = f.write("me")


print(a)

# it can't both read and write at the same time 