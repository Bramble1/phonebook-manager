#Create three classes: A bird parent class and then an owl and dodo class. Using the four object oriented principles being: inheritance,polymorphism,abstraction,encapsulation.
#Bird class will be an abstract class, then the other two classes will inherit the abstract parent class, and overload any default methods with their own using polymorphism

import sys
from abc import ABC,abstractmethod

#abstract class Bird with an abstract method which the class gets inherited by the subclasses
#and using polymorphism we overload the abstract function. As well as already being encapsulated
#in their own respective classe 

class Bird(ABC):

    @abstractmethod
    def speak(self):
        pass


class Owl(Bird):
    def speak(self):
        print("I'm an owl")


class Dodo(Bird):
    def speak(self):
        print("I'm a dodo")

#Main
#____________________________



owl = Owl()
owl.speak()

dodo=Dodo()
dodo.speak()
