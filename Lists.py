xy = ['ciao', 1, 2, 12.3, 15]
print(xy)

i = 1
while i < 6:
  print(i)
  i += 1

fruits = ["apple", "banana", "cherry"]
for x in fruits:
      if x == "banana":
          break
      print(x)
for x in range(6):
        print(x)
for x in range(2, 6):
  print(x)

states = ('NY', 'LS', 'NJ')

for i in states:
    print(i)

for x in range(2, 30, 3):
        print(x)


def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("Albania")
my_function()


def my_function(x):
  return 5 * x

print(my_function(3))



myfunc = lambda x,y: x*y
print(myfunc(3,6))


def myfunc(n):
  return lambda i: i*n

doubler = myfunc(2)
print(str(doubler))
tripler = myfunc(3)
val = 11
print("Doubled: " + str(doubler(val)) + ". Tripled: " + str(tripler(val)))


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()