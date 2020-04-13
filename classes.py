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

    def punch(self) -> None:



M = Person('Mark', 150, 50)
T = Person('Trevor', 180, 40)

print(str(M))
print(str(T))


