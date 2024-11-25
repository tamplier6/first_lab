from typing import List, Optional

class Animal:
    def __init__(self, id: int, name: str, species: str, age: int):
        self.id = id
        self.name = name
        self.species = species
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.species}, {self.age} years old)"

    def eat(self, food: str):
        print(f"{self.name} ест {food}")

    def sleep(self):
        print(f"{self.name} спит")

class Shelter:
    def __init__(self, id: int, name: str, address: str, capacity: int):
        self.id = id
        self.name = name
        self.address = address
        self.capacity = capacity
        self.animals: List[Animal] = []  # Список животных в приюте

    def admit_animal(self, animal: Animal) -> bool:
        if len(self.animals) < self.capacity:
            self.animals.append(animal)
            print(f"Животное {animal.name} принято в приют '{self.name}'.")
            return True
        else:
            print(f"Приют '{self.name}' переполнен. Животное {animal.name} не может быть принято.")
            return False

    def release_animal(self, animal_id: int) -> Optional[Animal]:
        for animal in self.animals:
            if animal.id == animal_id:
                self.animals.remove(animal)
                print(f"Животное {animal.name} выпущено из приюта '{self.name}'.")
                return animal
        print(f"Животное с ID {animal_id} не найдено в приюте '{self.name}'.")
        return None

    def list_animals(self):
        if self.animals:
            print(f"Список животных в приюте '{self.name}':")
            for animal in self.animals:
                print(f"- {animal}")
        else:
            print(f"Приют '{self.name}' пуст.")

class Breed:
    def __init__(self, id: int, name: str,  characteristics: str) :
        self.id = id
        self.name = name
        self.characteristics = characteristics
    
    def describe_breed(self, name: str, characteristics: str):
        print(f"Порода собаки: {name}, характеристики - {characteristics}")

class Owner:
    def __init__(self, id: int, name: str, phone_number: str):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.animals: List[Animal] = []

    def adopt_animal(self, animal: Animal) -> bool:
        self.animals.append(animal)
        print(f"Владелец {self.name} приютил {animal.name}")
        return True
    
    def remove_animal(self, animal: Animal) -> bool:
        if animal in self.animals:
            self.animals.remove(animal)
            print(f"Животное {animal.name} удалено у владельца {self.name}.")
            return True
        else:
            print(f"Животное {animal.name} не найдено у владельца {self.name}.")
            return False

class Veterinarian:
    def __init__(self, id: int, name: str, specialization: str):
        self.id = id
        self.name = name
        self.specialization = specialization

    def __str__(self):
        return f"{self.name}, Специализация: {self.specialization}"

    def schedule_appointment(self, owner: Owner, animal: Animal):
        print(f"Запланирован прием для животного {animal.name} владельца {owner.name} у ветеринара {self.name}.")

    def perform_checkup(self, animal: Animal):
        print(f"Ветеринар {self.name} проводит осмотр животного {animal.name}.")

