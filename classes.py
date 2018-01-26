class OurClass():

    def __init__(self):
        self.name = "Miles"

our_class = OurClass()

print (our_class.name)


class Dog():


    def __init__(self, name, happiness_level=5):
       self.name = name
       self.happiness_level = 5

    def wag_tail(self, n):
       self.happiness_level = (n * 5) + self.happiness_level

dog = Dog('spot')



dog.wag_tail(5)

print (dog.happiness_level)

class Cat():


   def __init__(self, name, laziness_level, location):
       self.name = name
       self.laziness_level = laziness_level
       self.location = 'Denver'


   def sense_earthquake(self, earthquake):
       if earthquake == True:
           self.location = 'Gone dark'
       else:
           self.location = self.location

cat_earth = Cat('spot', 3, 'Denver')

cat_earth.sense_earthquake(True)
print (cat_earth.location)

class Car():

    def __init__(self, model, color, tank_size):
        self.model = model
        self.color = color
        self.tank_size = tank_size
        self.gallons_of_gas = self.tank_size

    def drive(self, miles_driven):
        self.gallons_of_gas -= miles_driven / 10

car = Car('tesla', 'red', 16)

car.drive(50)

print (car.gallons_of_gas)
