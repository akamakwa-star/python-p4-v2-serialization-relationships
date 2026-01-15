
class Animal:
    def __init__(self, name=None, species=None):
        self.name = name
        self.species = species

    def to_dict(self):
        return {
            "name": self.name,
            "species": self.species
        }


class Enclosure:
    def __init__(self, name=None, capacity=None):
        self.name = name
        self.capacity = capacity

    def to_dict(self):
        return {
            "name": self.name,
            "capacity": self.capacity
        }


class Zookeeper:
    def __init__(self, name=None, experience_years=None):
        self.name = name
        self.experience_years = experience_years

    def to_dict(self):
        return {
            "name": self.name,
            "experience_years": self.experience_years
        }
