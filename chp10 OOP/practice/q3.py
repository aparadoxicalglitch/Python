class Sample:
    a = "Harry"

obj = Sample()
obj.a = "Vikky"
# Sample.a = "Vikky"  --> to change class attribute

print(Sample.a)
print(obj.a)