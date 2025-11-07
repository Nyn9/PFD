from dataclasses import dataclass, field
import random
import string


def generate_id() -> str:
    """Generate a random 15-character lowercase string as an ID."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Class representing a student with automatic ID and login generation."""
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """Generate the login after initialization."""
        self.login = self.name[0] + self.surname.lower()
