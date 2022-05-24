import time
print("Hi this program will calculate the force, mass and  acceleration of something.")
time.sleep(1.)

print("")

print("if you want to now the force of something write force.")
time.sleep(.8)
print("if you want to now the mass of something write mass.")
time.sleep(.8)
print("if you want to now the acceleration of something write acceleration.")
time.sleep(.8)

print("")

option = (input("Hello choose one of the above options: "))

if option == "mass":
    force = int(input("Put here the force in Newtons: "))
    time.sleep(.3)
    acc = int(input("Put here the acceleration in m/s2: "))
    time.sleep(.9)
    mass = force / acc
    print(mass, "Kg")

if option == "force":
    mass = int(input("Put here the mass in kilos: "))
    time.sleep(.3)
    acc = int(input("Put here the acceleration in m/s2: "))
    time.sleep(.9)
    force = mass * acc
    print(force, "Newtons")

if option == "acceleration":
    mass = int(input("Put here the mass in kilos: "))
    time.sleep(.3)
    force = int(input("Put here the force in Newtons: "))
    time.sleep(.9)
    force = mass / force
    print(force, "Newtons")


time.sleep(1000000)
