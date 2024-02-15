class Car: # Определяет среднестатистическую машину
    vehicle_type = "Car"

    def __init__(self, name: str, last_name: str):
        self.name = name
        self._last_name = last_name  # Данная информация является секретной
                                      # И не должна быть известна рядовому пользователю

    def isfast(self):  # Данный метод позволяет узнать, насколько быстрая машина
        print("Yes")

    def isquiet(self):  # Данный метод позволяет узнать, тихая ли машина (будет унаследован)
        print("Yes")

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}')"


class SUV(Car): # Другая разновидность машины
    pass

    def isfast(self):  # Данный метод был перегружен из-за того, что внедорожник медленнее обычной машины
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

