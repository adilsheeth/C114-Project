a = 33
b = '33'

if b > a:
    print("B is greater than A")
elif a == b:
    print("A is equal to B")
else:
    print("A is less than B")

# Result: TypeError, > not supported between instances of str and int.