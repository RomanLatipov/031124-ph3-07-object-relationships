# One to Many #
from classes.models import Car, Garage

# Many to Many #
from classes.models import Doctor, Patient, Appointment

# HARD MODE # (You may need to make more models to make this work!)
from classes.models import Student, Enrollment, Course

# SEED DATA GOES BELOW

g1 = Garage(address = "11 Broadway")
g2 = Garage(address = "123 Main Street")

c1 = Car(make="BMW", model="E30", license_plate="v34trfe", garage=g1)
c2 = Car(make="BMW", model="X6", license_plate="h9cibhcuui", garage=g2)
c3 = Car(make="Mercedes", model="X4", license_plate="ffewfcuui", garage=g1)
c4 = Car(make="Toyota", model="6e", license_plate="h098hhcfefei", garage=g2)

p1 = Patient("Bob", "Ross")
p2 = Patient("dick", "tracey")

d1 = Doctor("Tom Jerry", "Proctologist")
d2 = Doctor("Joe Biden", "dentist")

a1 = Appointment(d1, p1)
a2 = Appointment(d2, p2)
a3 = Appointment(d1, p2)
a4 = Appointment(d2, p1)

s1 = Student("Bob Ross")
c1 = Course("Biology")

e1 = Enrollment("01/01/25", s1, c1)