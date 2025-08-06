import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Slice the family list from start to end index."""
    try:
        if not isinstance(family, list):
            raise ValueError("Family must be a list.")
        if not isinstance(start, int) or not isinstance(end, int):
            raise ValueError("Start and end indices must be integers.")
        arr = np.array(family)
        if arr.ndim != 2:
            raise ValueError("Family must be a 2D array.")
        print(f"My shape is: {arr.shape}")
        new_arr = arr[start:end]
        print(f"My new shape is: {new_arr.shape}")
        return new_arr.tolist()
    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    """Main function to test the slice_me function."""
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    print(slice_me(family, 0, 5))
    print(slice_me(family, 5, -2))


if __name__ == "__main__":
    main()
