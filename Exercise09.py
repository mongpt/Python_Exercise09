# 9.1
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

# 9.2
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


# 9.3
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

#9.4
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


