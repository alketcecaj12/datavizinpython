# list = mulable collection of different types
x = [1, 2, 'x', 'y']
# tuple - similar to list but immutable (values cannot be changed)
y = ('a', 1)
# dictionary - hash table / hash map
z = { 1: 'x', 'y': 2 }
# set
k = set([1, 2, 'a', 'b'])

# adding data
x[0] = True     # dictionary
x. append(7)  # list
print(x)
# removing data
x.remove(2)  # lists, sets
del z[1]          # dictionary
print(x)
print(z)
# composing
xy = [ 2*i + 1 for i in range(5) ]    # list of first 5 odd numbers
print(xy)
xz = { i: i*i for i in range(5) }        # mapping numbers to their squares
print(xz)
# nesting them
xk = [ (i, 2*i) for i in range(5) ]    # list of tuples
print(xk)

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

m = int(input("Please enter an integer: "))
if m < 0:
   m = 0
   print("m vale "+m)
else:
    print(m)