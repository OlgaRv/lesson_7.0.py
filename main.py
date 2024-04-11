# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
# Дополнительно:
# Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл и
# возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        pass
    def eat(self):
        pass
    def get_info(self):
        pass
class Bird(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def make_sound(self):
        print(f"{self.name} поет")
    def eat(self):
        print(f"{self.name} клюёт")
    def fly(self):
        print(f"{self.name} летает")
    def get_info(self):
        with open('zoo.txt', 'a', encoding="UTF-8") as f:
            print(f"Это {self.name}, ему {self.age} лет, у него {self.color} цвет перьев", file=f)
class Mammal(Animal):
    def __init__(self, name, age, legs):
        super().__init__(name, age)
        self.legs = legs
    def make_sound(self):
        print(f"{self.name} издает громкие звуки")
    def eat(self):
        print(f"{self.name} лижет и грызёт пищу")
    def lactate(self):
        print(f"{self.name} вскармливает детенышей молоком")
    def get_info(self):
        with open('zoo.txt', 'a', encoding="UTF-8") as f:
            print(f"Это {self.name}, ему {self.age} лет, у него {self.legs} ноги", file=f)

class Reptile(Animal):
    def __init__(self, name, age, lenght):
        super().__init__(name, age)
        self.lenght = lenght

    def make_sound(self):
        print(f"{self.name} обычно шипит")
    def eat(self):
        print(f"{self.name} заглатывает пищу")
    def lay_eggs(self):
        print(f"{self.name} размножается откладыванием яиц")
    def get_info(self):
        with open('zoo.txt', 'a', encoding="UTF-8") as f:
            print(f"Это {self.name}, ему {self.age} лет, его длина {self.lenght} метров", file=f)

class ZooKeeper():
    def __init__(self, name):
        self.name = name
        self.status = "Keeper"
    def feed_animal(self, name):
        with open('zoo.txt', 'a', encoding="UTF-8") as f:
            print(f"{self.name} кормит зверей и птиц", file=f)

    def get_status(self):
        return self.status

class Veterinarian():
      def __init__(self, name):
          self.name = name
          self.status = "Veterinar"
      def heal_animal(self, name):
        with open('zoo.txt', 'a', encoding="UTF-8") as f:
            print(f"{self.name} лечит животных", file=f)

      def get_status(self):
        return self.status

class Zoo():
    def __init__(self):
        self.animals_list = []
        self.persons_list = []

    def add_animal(self, animal):
        self.animals_list.append(animal)
        print("Животное/птица добавлено в список")

    def get_animals_list(self):
        return self.animals_list

    def add_person(self, person):
        self.persons_list.append(person)

    def get_persons_info(self):
        for person in self.persons_list:
            status = person.get_status()
            if status == "Keeper":
                print(person.feed_animal(person.name))
            else:
                print(person.heal_animal(person.name))

bird = Bird("фламинго", 3 , "розовый")
bird.make_sound()
bird.eat()
bird.fly()

mammal = Mammal("ягуар", 5, 4)
mammal.make_sound()
mammal.eat()
mammal. lactate()

reptile = Reptile("питон", 7, 15)
reptile.make_sound()
reptile.eat()
reptile.lay_eggs()

animals_select = [bird, mammal, reptile]
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

animal_sound(animals_select)

zoo = Zoo()
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)
for animal in zoo.get_animals_list():
    print(animal.get_info())

petr = ZooKeeper("Петр")
ivan = ZooKeeper("Иван")
alex = ZooKeeper("Александр")

ann = Veterinarian("Анна")
iren = Veterinarian("Ирина")
lili = Veterinarian("Лилия")

zoo.add_person(petr)
zoo.add_person(ivan)
zoo.add_person(alex)
zoo.add_person(ann)
zoo.add_person(iren)
zoo.add_person(lili)
zoo.get_persons_info()
