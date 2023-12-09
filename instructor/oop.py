class Dog():
  total_dogs = 0

  def __init__(self, name="", age=0, color=''):
    self.name = name
    self.age = age
    self.color = color
    Dog.total_dogs += 1


    print(name, "created:", self)

  def bark_hello(self):
    print("Woof! I am called", self.name, "I am", self.color, "and I am", self.age, "human-years old.")
    print("There are", Dog.total_dogs, "dogs in this room!")



gracie = Dog("Gracie", 5, "black")
gracie.bark_hello()  # Woof! I am called Gracie and I am 8 human-years old.'
spitz = Dog("Spitz", 5, "white")  # lead dog
spitz.bark_hello()   # Woof! I am called Spitz and I am 5 human-years old.'
buck = Dog("Buck", 3, "brown")  # upstart newcomer
buck.bark_hello()    # Woof! I am called Buck and I am 3 human-years old.


# random = Dog()

# random.bark_hello()  # Woof! I am called  and I am 0 human-years old.

# print(gracie)
# print({'jello': 'hello'})

print('*******************************************')

class Parent():
  def __init__(self):
    self.first_name = "Lorelei"
    self.last_name = "Gilmore"
    print('-------')
    print("Parent initialized:", self)
    print('-------')
  def hello(self):
    print(f"Hey, I'm {self.first_name} {self.last_name}. Welcome to the Dragonfly!")

class Child(Parent):
  def __init__(self):
    super().__init__()
    self.first_name = "Rory"
    print('-------')
    print("Child initialized:", self)
    print('-------')

mom = Parent()
print('*******************************************')
daughter = Child()

print('*******************************************')

mom.hello()
daughter.hello()

print('*******************************************')
print(daughter.last_name)


print('*******************************************')
