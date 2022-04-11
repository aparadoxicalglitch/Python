class Sample: 
    def __init__(slf, name):
        slf.name = name

obj = Sample("Harry") 
print(obj.name) 
 # we can use any name instead of self and will compile without any error but it may counfuse the other person and is best to ues self only