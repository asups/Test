# class Parent:
#     # def __init__(self, math):
#     #     self.math = math
#
#     def drive(self, s):
#         print(s)
#
# class Child(Parent):
#     pass
#
# sam = Child()
# sam.drive('ехать')

# class Animal:
#     def make_sound(self, s):
#         print(s)
#
# class Dog(Animal):
#     def dog(self):
#         print('гав гав')
#
#
# class Cat(Animal):
#     def cat(self):
#         print('мяу')
#
# class Cow(Animal):
#     def cow(self):
#         print('му му')
#
# # Dog.make_sound('Гав, гав')
# # Cat.make_sound("Мяу")
# # Cow.make_sound("Муму")
#
# dog = Dog()
# dog.dog()
#
# cat = Cat()
# cat.cat()
#
# cow = Cow()
# cow.cow()

class Animal:
    def make_sound(self, s):
        print(s)

class Dog(Animal):
    pass

class Cat(Animal):
    pass
class Cow(Animal):
    pass

dog = Dog()
dog.make_sound('Гав')

cat = Cat()
cat.make_sound('Мяу')

cow = Cow()
cow.make_sound('Му му')