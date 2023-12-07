#4i)
for k in range(1, 6):
    for j in range(1, k + 1):
        print(j, end="")
    print()

 #ii)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Test the function with n = 5
result = factorial(5)
print(result)

#iii)

def sum_of_two_numbers(a, b):
    return a + b

# Testing the function
a = 3
b = 4
result = sum_of_two_numbers(a, b)
print(result)

#iv)
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print("Brand:", self.brand)
        print("Year:", self.year)
        
my_object=Car("Toyota",2022)
my_object.display_info()
        

# Define a class
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

#v)
# Create an instance of the class
my_object = MyClass("Esther", 22)
my_object.display_info()