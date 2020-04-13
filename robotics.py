class Bin:
    """Represents a storage bin
    Attrs:
        id(int): shows the id of the bin
        location(str): shows the bin's location
        part_id(str): shows id of a single Part object
        qty_in_bin(int): shows how many of said Part is in the bin
    """
    def __init__(self, id: int, location: str, part_id: str, qty_in_bin: int):
        "Initializes description of the bin"
        self.id = id
        self.location = location
        self.part_id = part_id
        self.qty_in_bin = qty_in_bin

    