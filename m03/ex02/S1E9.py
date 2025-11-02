from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class for a character."""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize the character with a first name and alive status."""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Set the character's status to dead."""
        self.is_alive = False

    @abstractmethod
    def introduce(self):
        """Introduce the character."""
        pass


class Stark(Character):
    """Representing the Stark family."""
    def introduce(self):
        """Introduce the Stark character."""
        print(f"I am {self.first_name} of House Stark.")
