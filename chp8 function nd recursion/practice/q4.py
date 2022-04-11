# n! = (n-1)! * n 
# sum(n) = sum(n-1) + n
a=int(input("Enter a number\n"))

def sum_recursive(a):
    if a<=1:
        return 1
    return a+ sum_recursive(a-1)

x=sum_recursive(a)
print("The sum is: ",x)