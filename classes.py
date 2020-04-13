class Person:
    """ Represents a person
    Attrs:
        name(str): Person's first and last
        height(int): in centimetres
        strength(int): How strong the person is
        hp(int): Health Points Out of 100 (starts at 100)
    """
    def __init__(self, name: str, height: int, strength: int):
        "Initializes description of person "
        self.name = name
        self.height = height
        self.strength = strength
        self.hp = 100

    def __str__(self) -> str:
        "Shows information of person"
        return f"Name: {self.name}, HP: {self.hp}"

    def introduce(self) -> None:
        "Simulates the person introducing himself"
        return f"Hello, my name is {self.name}"

    def punch(self, other_person):
        "Simulates a person punching someone else, in which the latter loses health"
        other_person.hp -= 10
        return f"{self.name} punched {other_person.name}"

    def eat(self) -> None:
        "Simulates a person eating food and regaining health"
        self.hp = 100


M = Person('Mark', 150, 50)
T = Person('Trevor', 180, 40)

print(str(M))
print(str(T))


