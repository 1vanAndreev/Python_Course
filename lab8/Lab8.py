class Car: 
    vehicle_type = "Car"

    def __init__(self, name: str, last_name: str):
        self.name = name
        self._last_name = last_name  
                                    
    def isfast(self):  
        print("Yes")

    def isquiet(self):  
        print("Yes")

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}')"

class SUV(Car): 
    pass

    def isfast(self):  
        print("No")
car = Car("Toyota", "Camry")
suv = SUV("Ford", "Explorer")
print("Имя? -> ", end="")
print(car)
print("Тип транспортного средства? -> ", end="")
print(car.vehicle_type)
print("Быстрая ли машина? -> ", end="")
car.isfast()
print("Тихая ли машина? -> ", end="")
car.isquiet()
print("")
print("Имя? -> ", end="")
print(suv)
print("Тип транспортного средства? -> ", end="")
print(suv.vehicle_type)
print("Быстрая ли машина? -> ", end="")
suv.isfast()
print("Тихая ли машина? -> ", end="")
suv.isquiet()

