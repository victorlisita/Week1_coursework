from classes import Person


def test_person():
    "testing the person class"
    man = Person("Mark", 160, 35)
    assert man.name == "Mark"
    assert man.height == 160
    assert man.strength == 35
    assert man.hp == 100


def test_introduce():
    "testing the introducing function"
    man = Person("Mark", 160, 35)
    assert man.introduce == "Hello, my name is Mark"


def test_punch():
    "testing the punch function"
    man = Person("Mark", 160, 35)
    other_man = Person('Trevor', 180, 40)
    assert man.punch == "Mark punched Trevor"
    assert other_man.hp == 90


def test_eat():
    "testing the eat function"
    man = Person("Mark", 160, 35)
    man.hp = 50
    man.eat()
    assert man.hp == 100
