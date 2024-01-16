#!/usr/bin/env python
# coding: utf-8

# In Python, a class is a blueprint or a template for creating objects. An object is an instance of a class. Let's break down the concepts of classes and objects:

# In[1]:


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says Woof!")

# Creating an object of the Dog class
my_dog = Dog("Buddy", 3)

# Accessing attributes and calling methods
print(my_dog.name)  # Output: Buddy
my_dog.bark()       # Output: Buddy says Woof!


# Class:
# A class is a user-defined data type that defines a blueprint for creating objects. It encapsulates data (attributes) and functions (methods) that operate on the data. The syntax for creating a class in Python is as follows:

# class_variable: These are attributes shared by all instances of the class.
# __init__: This is a special method (constructor) that gets called when an object is created. It initializes the object's attributes.
# self: It represents the instance of the class. By convention, it is named self, but you can name it differently if you want.
# method1 and method2: These are functions that operate on the object's data.

# Object:
# An object is an instance of a class. When a class is defined, no memory is allocated for the data members and methods. However, when an object is created, memory is allocated for the data members, and methods are shared among all instances of the class. You can create multiple objects from the same class, and each object will have its own set of attributes.

# # Encapsulation
# It is one of the fundamental principles of object-oriented programming (OOP), and it involves bundling the data (attributes) and the methods (functions) that operate on the data into a single unit known as a class. This unit restricts access to some of its components, providing a way to control the interaction with the internal state of an object. The primary goal of encapsulation is to hide the internal details of an object and expose only what is necessary for the outside world.
# 
# Here are key aspects of encapsulation in Python:
# 
# Access Modifiers:
# 
# In Python, there is no strict enforcement of access modifiers like in some other programming languages (e.g., Java or C++). However, there is a convention that is commonly followed to indicate the visibility of attributes and methods:
# Public: Members are accessible from outside the class. No underscore before the name (e.g., self.name).
# Protected: Members should not be accessed from outside the class, but they can be accessed in derived classes. A single underscore before the name (e.g., _protected_variable).
# Private: Members should not be accessed from outside the class. A double underscore before the name (e.g., __private_variable).

# In[12]:


class Example:
    def __init__(self):
        self.public_variable = "Public"
        self._protected_variable = "Protected"
        self.__private_variable = "Private"

obj = Example()

print(obj.public_variable)          # Accessible
print(obj._protected_variable)      # Accessible (convention, not enforced)
#print(obj.__private_variable)     # Error (NameError: name '_Example__private_variable' is not defined)


# In[14]:


class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Getter methods
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    # Setter methods
    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        if age > 0:
            self._age = age

student = Student("Alice", 20)

# Using getter methods
print(student.get_name())  # Output: Alice
print(student.get_age())   # Output: 20

# Using setter methods
student.set_name("Bob")
student.set_age(25)

print(student.get_name())  # Output: Bob
print(student.get_age())   # Output: 25




# # Inheritance: 
# it is another key concept in object-oriented programming (OOP) that allows a class (subclass or derived class) to inherit attributes and methods from another class (superclass or base class). Inheritance promotes code reuse and the creation of a hierarchy of classes.

# Base Class (Superclass):
# 
# The class whose attributes and methods are inherited by another class is known as the base class or superclass.
# The base class provides a common set of features that can be shared among multiple derived classes.

# In[4]:


class Animal:
    def __init__(self, name):
        self.name = name
 
    def speak(self):
        pass  # Abstract method

# Animal is the base class


# In[15]:


class Dog(Animal):  # Inheriting from the Animal class
    def bark(self):
        print("Woof!")

class Cat(Animal):  # Inheriting from the Animal class
    def meow(self):
        print("Meow!")


# Super Function:
# 
# The super() function is used to call a method from the base class. It is often used in the derived class to invoke the constructor or methods of the base class.

# In[7]:


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


# Multiple Inheritance:
# 
# A class can inherit from more than one base class. This is known as multiple inheritance.
# While it provides flexibility, it also introduces challenges such as the diamond problem, where the same method may be inherited from two different paths.
# Example:

# In[8]:


class A:
    def method(self):
        print("Method from class A")

class B:
    def method(self):
        print("Method from class B")

class C(A, B):  # Multiple inheritance from classes A and B
    pass

obj = C()
obj.method()  # Output: Method from class A (Method from class A is called due to the order of inheritance)


# In[9]:


class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguin can't fly")

def demonstrate_flying(bird):
    bird.fly()

sparrow = Sparrow()
penguin = Penguin()

demonstrate_flying(sparrow)  # Output: Sparrow can fly
demonstrate_flying(penguin)  # Output: Penguin can't fly




# Abstraction:
# 
# Abstraction involves hiding the complex implementation details and exposing only the necessary features of an object.
# Abstract classes and interfaces are used to achieve abstraction in Python.

# In[10]:


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

circle = Circle(5)
rectangle = Rectangle(4, 6)

print(circle.area())     # Output: 78.5
print(rectangle.area())  # Output: 24


# # Polymorphism:
# 
# Polymorphism is one of the four fundamental principles of object-oriented programming (OOP), and it refers to the ability of objects of different classes to be treated as objects of a common base class. There are two main types of polymorphism: compile-time (or static) polymorphism and runtime (or dynamic) polymorphism. In Python, runtime polymorphism is more common.

# Different classes work as a instance of same class.

# # Method overloading & Overriding

# Method Overloading:
# Method overloading in Python is achieved through a feature called "default values" or using the *args and **kwargs syntax in function definitions. Python does not natively support method overloading in the traditional sense where multiple methods with the same name are defined in a class with different parameter lists.

# In[16]:


class Calculator:
    def add(self, a, b = 0 , c=0):
        return a + b + c

# Creating an object of the class
calc = Calculator()

# Calling the method with different argument combinations
result1 = calc.add(1)
result2 = calc.add(1, 2)
result3 = calc.add(1, 2, 3)


print(result1)  # Output: 1
print(result2)  # Output: 3
print(result3)  # Output: 6




# In[17]:


class Calculator:
    def add(self, *args):
        return sum(args)

# Creating an object of the class
calc = Calculator()

# Calling the method with different numbers of arguments
result1 = calc.add(1)
result2 = calc.add(1, 2)
result3 = calc.add(1, 2, 3)

print(result1)  # Output: 1
print(result2)  # Output: 3
print(result3)  # Output: 6



# Method Overriding:
# Method overriding occurs when a derived class provides a specific implementation for a method that is already defined in its base class. In Python, this is achieved by creating a method with the same name in the derived class.

# In[18]:


class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Creating objects of the classes
animal = Animal()
dog = Dog()
cat = Cat()

# Calling the speak method
animal.speak()  # Output: Animal speaks
dog.speak()     # Output: Dog barks
cat.speak()     # Output: Cat meows



# In this example, the speak method is overridden in the Dog and Cat classes. When calling speak on a Dog object or a Cat object, the overridden method in the respective subclass is executed.
# 
# Method overriding is crucial for achieving polymorphism, where objects of different classes can be treated as objects of a common base class. It allows for flexibility in designing and using classes in a hierarchy.
# 
# 
# 
# 
# 
# 
# 

# # Multithreading

# Multithreading in Python refers to the concurrent execution of multiple threads (smaller units of a process) to perform parallel tasks. Python provides a built-in threading module that allows you to create and manage threads. Each thread runs in its own memory space but shares the same resources of a process, such as global variables.

# In[20]:


import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Thread {threading.current_thread().name}: {i}")

# Create two threads
thread1 = threading.Thread(target=print_numbers, name="Thread 1")
thread2 = threading.Thread(target=print_numbers, name="Thread 2")

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both threads have finished.")



# Class Methods and Static Methods:
# 
# Class Methods: Methods that are bound to the class and not the instance of the class.
# Static Methods: Methods that are defined within a class but do not have access to class or instance-specific data.

# In[21]:


class MyClass:
    class_variable = "Class Variable"

    @classmethod
    def class_method(cls):
        print(f"Accessing class variable: {cls.class_variable}")

    @staticmethod
    def static_method():
        print("This is a static method.")


# In[22]:


# Operator Overloading:

#The ability to define how operators behave for user-defined objects.

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"
    
    


# In[ ]:





# In[ ]:





# In[ ]:




