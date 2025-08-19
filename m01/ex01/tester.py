from array2D import slice_me


def main():
    """Main function to test the slice_me function."""
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]

    try:
        print(slice_me(family, 0, 2))
    except Exception as e:
        print(f"Error: {e}")
    try:
        print(slice_me(family, 1, -2))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
