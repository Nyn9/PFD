class calculator:
    """A simple calculator class to perform basic arithmetic operations."""

    def __init__(self, n: list[float]) -> None:
        """Initialize the calculator with a list of numbers."""
        self.numbers = n

    def __add__(self, object) -> None:
        self.numbers = [x + object for x in self.numbers]
        print(self.numbers)

    def __mul__(self, object) -> None:
        self.numbers = [x * object for x in self.numbers]
        print(self.numbers)

    def __sub__(self, object) -> None:
        self.numbers = [x - object for x in self.numbers]
        print(self.numbers)

    def __truediv__(self, object) -> None:
        if object == 0:
            print("Error: Division by zero is not allowed.")
            return
        self.numbers = [x / object for x in self.numbers]
        print(self.numbers)
