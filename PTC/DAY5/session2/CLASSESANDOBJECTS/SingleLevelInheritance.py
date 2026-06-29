class Dog:
    def sound():
        print("BOW BOW")
    def eat(self):
        print("Dog is eating")
class Cat(Dog):
    def sound():
        print("MEOW MEOW")
#instance
d=Cat()
d.eat()
