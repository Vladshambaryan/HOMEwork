
class Animal:

    def eat(self):
        print("Я могу есть!")

    def sleep(self):
        print("я могу спать!")


# derived class
class Dog(Animal):

    def bark(self):
        print("я говорю гаф гаф!!")


# Create object of the Dog class
dog1 = Dog()

# Calling members of the base class
dog1.eat()
dog1.sleep()

# Calling member of the derived class
dog1.bark();
