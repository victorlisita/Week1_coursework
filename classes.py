class Person:
    """
    Attrs:
        name(str): Person's first and last
        height (int): in centimetres
        strength (int): How strong the person is
        hp (int): Health Points Out of 100 (starts at 100)
    """
    def __init__(self, name, height, strength):
        self.name = name
        self.height = height
        self.strength = strength
        self.hp = 100

    def __str__(self) -> str:
        return f"Name: {self.name}, HP: {self.hp}"

M = Person('Mark', 150, 50)
T = Person('Trevor', 180, 40)

print(str(M))
print(str(T))


