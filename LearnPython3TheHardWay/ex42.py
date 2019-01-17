## Animal is a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is an animal
class Dog(Animal):

    def __init__(self,name):
        ##Dog has a name
        self.name = name

# Cat is an animal
class Cat(Animal):

    def __init__(self,name):
        ## Cat has a name
        self.name = name

# Person
class Person(object):
    def __init__(self, name):
        ## Person has a name
        self.name = name

        #Person has a pet of some kind
        self.pet = None

## Employee is a person
class Employee(Person):

    def __init__(self, name, salary):
        # super refers to the parent class
        super(Employee,self).__init__(name)
        ## call the parent class person before this
        self.salary = salary

## Fish is an object
class Fish(object):
    pass

## Salmon is a fish
class Salmon(Fish):
    pass

## Halibut is a fish
class Halibut(Fish):
    pass

#Rover is a dog
rover = Dog("Rover")

## satan is a cat
satan = Cat("Satan")

## mary is a person
mary = Person("Mary")

## mary has a pet called satan who is a cat
mary.pet = satan

## frank is an employee with a salary of 120,000
frank = Employee("Frank",120000)

## frank has a pet called rover who is a dog
frank.pet = rover

## flipper is a fish
flipper = Fish()

## crouse is a salmon
crouse = Salmon()

## harry is a Halibuts
harry = Halibut()

# print franks pets name using dot walking
print(frank.pet.name)
