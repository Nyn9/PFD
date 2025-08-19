import cv2
import numpy as np


def ft_load(path: str) -> np.array:
    """Load an image from the specified path and return its pixel data."""
    if not isinstance(path, str):
        raise AssertionError("Path must be a string.")
    if not path.endswith('.jpg') and not path.endswith('.jpeg'):
        raise AssertionError("Path must be .jpg or .jpeg image file.")
    try:
        with open(path, 'rb'):
            pass
    except (FileNotFoundError, PermissionError, OSError):
        raise AssertionError("Image could not be loaded.")
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise AssertionError("Image could not be loaded.")
    return img


def main():
    """Main function to test the ft_load function."""
    try:
        ft_load('landscape.png')
    except Exception as e:
        print(f"Error: {e}")
    try:
        ft_load(5)
    except Exception as e:
        print(f"Error: {e}")
    try:
        ft_load('epacsdnal.jpg')
    except Exception as e:
        print(f"Error: {e}")
    try:
        ft_load('')
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
