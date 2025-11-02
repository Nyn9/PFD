from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        """Initialize Baratheon character."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """String representation of the Baratheon character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Official string representation of the Baratheon character."""
        return self.__str__()

    def introduce(self):
        """Introduce the Baratheon character."""
        print(f"I am {self.first_name} of House Baratheon.")


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """String representation of the Lannister character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Official string representation of the Lannister character."""
        return self.__str__()

    def introduce(self):
        """Introduce the Lannister character."""
        print(f"I am {self.first_name} of House Lannister.")

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """Class method to create a Lannister character."""
        return cls(first_name, is_alive)
