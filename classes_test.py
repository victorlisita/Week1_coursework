from classes import Person

def test_person():
    man = Person("Mark", 160, 35)
    assert man.name == "Mark"
    assert man.height == 160
    assert man.strength == 35
    assert man.hp == 100



