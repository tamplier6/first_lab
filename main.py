import json
from classes import Animal, Shelter, Owner, Veterinarian, load_from_json, save_to_json

def main():
    # Создание приюта
    shelter = Shelter(id=1, name="Приют Бирюлёво", address="Востряковский пр., вл10A/2, Москва", capacity=5)

    # Создание животных
    animal1 = Animal(id=1, name="Патрик", species="Собака", age=5)
    animal2 = Animal(id=2, name="Том", species="Кот", age=3)
    animal3 = Animal(id=3, name="Кузя", species="Попугай", age=2)

    # Добавление животных в приют
    shelter.admit_animal(animal1)
    shelter.admit_animal(animal2)
    shelter.admit_animal(animal3)

    # Вывод списка животных в приюте
    shelter.list_animals()

    # Сохранение данных приюта в JSON-файл
    shelter_data = {
        "id": shelter.id,
        "name": shelter.name,
        "address": shelter.address,
        "capacity": shelter.capacity,
        "animals": [
            {"id": animal.id, "name": animal.name, "species": animal.species, "age": animal.age}
            for animal in shelter.animals
        ]
    }
    save_to_json("shelter.json", shelter_data)

    # Загрузка данных из JSON-файла
    loaded_data = load_from_json("shelter.json")
    if loaded_data:
        print("\nДанные, загруженные из JSON:")
        print(json.dumps(loaded_data, ensure_ascii=False, indent=4))

    # Выпуск животного из приюта
    print("\nВыпуск животного с ID 1:")
    shelter.release_animal(1)


    # Повторный вывод списка животных
    print("\nОбновленный список животных:")
    shelter.list_animals()

    # Пример создания владельца
    owner = Owner(id=1, name="Игорь", phone_number="+7(918)666-66-66")
    owner.adopt_animal(animal2)

    # Пример обращения к ветеринару
    vet = Veterinarian(id=1, name="Доктор Мом", specialization="Хирург")
    vet.schedule_appointment(owner, animal2)
    vet.perform_checkup(animal2)

    # Попытка переполнения приюта
    print("\nПопытка добавить больше животных в приют:")
    for i in range(5):
        animal = Animal(id=10 + i, name=f"Животное_{i}", species="Собака", age=i)
        shelter.admit_animal(animal)

if __name__ == "__main__":
    main()
