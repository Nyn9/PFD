import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Slice the family list from start to end index."""
    try:
        assert isinstance(family, list), "Family must be a list."
        assert isinstance(start, int) and isinstance(end, int), \
            "Start and end indices must be integers."
        arr = np.array(family)
        assert arr.ndim == 2, "Family must be a 2D array."
        print(f"My shape is: {arr.shape}")
        new_arr = arr[start:end]
        print(f"My new shape is: {new_arr.shape}")
        return new_arr.tolist()
    except AssertionError as e:
        print(f"Error: {e}")


def main():
    """Main function to test the slice_me function."""
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]

    slice_me(family, "abc", 5)
    slice_me(family, 0, "abc")
    slice_me(None, 0, 5)

    family = [1.80, 78.4, 2.15, 102.7]
    slice_me(family, 0, 5)

    family = 10
    slice_me(family, 0, 5)

    family = "abc"
    slice_me(family, 0, 5)


if __name__ == "__main__":
    main()
