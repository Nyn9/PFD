class calculator:
    """A simple calculator class to perform basic arithmetic operations."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate and print the dot product of two vectors."""
        res = sum(x*y for x, y in zip(V1, V2))
        print("Dot product is:", res)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Calculate and print the addition of two vectors."""
        res = [float(x+y) for x, y in zip(V1, V2)]
        print("Add Vector is:", res)

    @staticmethod
    def sub_vec(V1: list[float], V2: list[float]) -> None:
        """Calculate and print the subtraction of two vectors."""
        res = [float(x-y) for x, y in zip(V1, V2)]
        print("Sub Vector is:", res)
