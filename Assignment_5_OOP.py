# write a simple python program that implements method overriding,method over loading,Method resolution order and define the terms first

# define the terms
# Method Overriding: This occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. The subclass method overrides the superclass method.
# Method Overloading: This refers to the ability to define multiple methods with the same name but different parameters (different number or types of parameters) within the same class.
# Method Resolution Order (MRO): This is the order in which Python looks for a method in a hierarchy of classes. It determines the order in which base classes are searched when a method is called on an instance of a class.

class Animal:   
    def make_sound(self):
        print("Some generic animal sound")

    def eat(self, food):
        print(f"Animal eats {food}")

class Dog(Animal):
    # Method Overriding (redefining parent's method)
    def make_sound(self):
        print("Bark!")

    # Method Overloading 
    def eat(self, food=None, times=None):
        if food is not None and times is not None:
            print(f"Dog eats {food} {times} times!")
        elif food is not None:
            super().eat(food)  # Calls parent's eat()
        else:
            print("Dog is not eating anything")

class Bulldog(Dog):
    # Method Overriding (further overriding)
    def make_sound(self):
        print("Bulldog Bark!")


animal = Animal()
dog = Dog()
bulldog = Bulldog()

# Method Overriding 
animal.make_sound()  # Output: "Some generic animal sound"
dog.make_sound()     # Output: "Bark!"
bulldog.make_sound() # Output: "Bulldog Bark!"

# Method Overloading Example (simulated)
dog.eat("bone")            # Output: "Animal eats bone" (calls parent's eat)
dog.eat("bone", 3)         # Output: "Dog eats bone 3 times!"
dog.eat()                  # Output: "Dog is not eating anything"

# Method Resolution Order (MRO) Example
print(Bulldog.__mro__)  # python checks in the order Bulldog → Dog → Animal → object.