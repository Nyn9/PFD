from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def set_eyes(self, color: str):
        """Set the eye color for the King."""
        self.eyes = color

    def set_hairs(self, color: str):
        """Set the hair color for the King."""
        self.hairs = color

    def get_eyes(self) -> str:
        """Get the eye color of the King."""
        return self.eyes

    def get_hairs(self) -> str:
        """Get the hair color of the King."""
        return self.hairs
