# Python_Exercise09
## 9. Fundamentals of object-oriented programming

1. Write a `Car` class that has the following properties: registration number, maximum speed, current speed and travelled distance. 
Add a class initializer that sets the first two of the properties based on parameter values. The current speed and travelled distance
of a new car must be automatically set to zero. Write a main program where you create a new car (registration number ABC-123, maximum speed 
142 km/h). Finally, print out all the properties of the new car.
```python
from tabulate import tabulate
class car:
    def __init__(self, regNumber, maxSpeed):
        self.regNum = regNumber
        self.maxSpeed = maxSpeed
        self.curSpeed = 0
        self.travelledDistance = 0
        self.carStatus = {}

    def info(self):
        self.carStatus = {
            "Registration Number": self.regNum,
            "Maximum speed": self.maxSpeed,
            "Current speed": self.curSpeed,
            "Travelled Distance": self.travelledDistance
        }
        return self.carStatus


carInfo = []
print("\n****** Exercise 9.1 ******")
newCar = car("ABC-123", 142)
carInfo.append(newCar.info())
print(tabulate(carInfo, headers="keys"))
```
Console output:
```
****** Exercise 9.1 ******
Registration Number      Maximum speed    Current speed    Travelled Distance
---------------------  ---------------  ---------------  --------------------
ABC-123                            142                0                     0
```
2. Extend the program by adding an `accerelate` method into the new class. The method should receive the change of speed (km/h) as a parameter. 
If the change is negative, the car reduces speed. The method must change the value of the `speed` property of the object. The speed of the car 
must stay below the set maximum and cannot be less than zero. Extend the main program so that the speed of the car is first increased by +30 km/h,
then +70 km/h and finally +50 km/h. Then print out the current speed of the car. Finally, use the emergency brake by forcing a -200 km/h change on 
the speed and then print out the final speed. The travelled distance does not have to be updated yet.
```python
class car:
    def __init__(self, regNumber, maxSpeed):
        self.regNum = regNumber
        self.maxSpeed = maxSpeed
        self.curSpeed = 0
        self.travelledDistance = 0

    def accelerate(self, speed):
        self.curSpeed += speed
        if self.curSpeed < 0:
            self.curSpeed = 0
        elif self.curSpeed > self.maxSpeed:
            self.curSpeed = self.maxSpeed
        return self.curSpeed

    def emergency(self):
        self.curSpeed -= 200
        if self.curSpeed < 0:
            self.curSpeed = 0
        return self.curSpeed


print("\n****** Exercise 9.2 ******")
newCar = car("ABC-123", 142)
newCar.accelerate(30)
newCar.accelerate(70)
newCar.accelerate(50)
print("Current car's speed after accelerating:", newCar.curSpeed)
newCar.emergency()
print("Current car's speed after emergency:", newCar.curSpeed)
```
Console output:
```
****** Exercise 9.2 ******
Current car's speed after accelerating: 142
Current car's speed after emergency: 0
```
3. Again, extend the program by adding a new `drive` method that receives the number of hours as a parameter. The method increases the travelled
distance by how much the car has travelled in constant speed in the given time. Example: The travelled distance of `car` object is 2000 km. The 
current speed is 60 km/h. Method call `car.drive(1.5)` increases the travelled distance to 2090 km.
```python
class car:
    def __init__(self, regNumber, maxSpeed):
        self.regNum = regNumber
        self.maxSpeed = maxSpeed
        self.curSpeed = 0
        self.travelledDistance = 0

    def accelerate(self, speed):
        self.curSpeed += speed
        if self.curSpeed < 0:
            self.curSpeed = 0
        elif self.curSpeed > self.maxSpeed:
            self.curSpeed = self.maxSpeed
        return self.curSpeed

    def emergency(self):
        self.curSpeed -= 200
        if self.curSpeed < 0:
            self.curSpeed = 0
        return self.curSpeed

    def drive(self, hours):
        self.travelledDistance += self.curSpeed * hours
        return self.travelledDistance

print("\n****** Exercise 9.3 ******")
newCar = car("ABC-123", 142)
newCar.accelerate(60)
print("Current car's speed:", newCar.curSpeed)
newCar.travelledDistance = 2000
print("Travelled distance:", newCar.travelledDistance, "km")
newCar.drive(1.5)
print("Travelled distance after 1.5 hours:", newCar.travelledDistance, "km")
```
Console output:
```
****** Exercise 9.3 ******
Current car's speed: 60
Travelled distance: 2000 km
Travelled distance after 1.5 hours: 2090.0 km
```
4. Now we will program a car race. The travelled distance of a new car is initialized as zero. At the beginning of the main program, create a list 
that consists of 10 car objects created using a loop. The maximum speed of each new car is a random value between 100 km/h and 200 km/h. 
The registration numbers are created as follows: "ABC-1", "ABC-2" and so on. Now the race begins. One per every hour of the race, the following 
operations are performed:
   - The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h. This is done using the `accerelate` method.
   - Each car is made to drive for one hour. This is done with the `drive` method.

The race continues until one of the cars has advanced at least 10,000 kilometers. Finally, the properties of each car are printed out formatted into a clear table.
```python
import random
from tabulate import tabulate
class car:
    def __init__(self, regNumber, maxSpeed):
        self.regNum = regNumber
        self.maxSpeed = maxSpeed
        self.curSpeed = 0
        self.travelledDistance = 0
        self.carStatus = {}

    def info(self):
        self.carStatus = {
            "Registration Number": self.regNum,
            "Maximum speed": self.maxSpeed,
            "Current speed": self.curSpeed,
            "Travelled Distance": self.travelledDistance
        }

    def accelerate(self, speed):
        self.curSpeed += speed
        if self.curSpeed < 0:
            self.curSpeed = 0
        elif self.curSpeed > self.maxSpeed:
            self.curSpeed = self.maxSpeed
        return self.curSpeed

    def emergency(self):
        self.curSpeed -= 200
        if self.curSpeed < 0:
            self.curSpeed = 0
        return self.curSpeed

    def drive(self, hours):
        self.travelledDistance += self.curSpeed * hours
        return self.travelledDistance

print("\n****** Exercise 9.4 ******")
carList = []
for i in range(1, 11):
    newCar = car("ABC-" + str(i), random.randint(100, 200))
    carList.append(newCar)

maxTravelledDistance = 0
while maxTravelledDistance < 10000:
    for i in range(10):
        carList[i].accelerate(random.randint(-10, 15))
        carList[i].drive(1)
        carList[i].info()
        if maxTravelledDistance < carList[i].travelledDistance:
            maxTravelledDistance = carList[i].travelledDistance

raceResult = []
for i in range(10):
    raceResult.append(carList[i].carStatus)
print(tabulate(raceResult, headers="keys"))
```
Console output:
```
****** Exercise 9.4 ******
Registration Number      Maximum speed    Current speed    Travelled Distance
---------------------  ---------------  ---------------  --------------------
ABC-1                              141               87                  2360
ABC-2                              175              141                  8226
ABC-3                              141              141                  6202
ABC-4                              117              117                  7943
ABC-5                              142              142                  5985
ABC-6                              175              166                  6550
ABC-7                              146              146                  5376
ABC-8                              142              142                  7046
ABC-9                              183              166                 10090
ABC-10                             131              120                  8800
```
