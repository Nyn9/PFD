import cv2
import numpy as np


def ft_load(path: str) -> np.array:
    """Load an image from the specified path and return its pixel data."""
    try:
        assert isinstance(path, str), "Path must be a string."
        assert path.endswith('.jpg') or path.endswith('.jpeg'), \
            "Path must be .jpg or .jpeg image file."
        with open(path, 'rb'):
            pass
        img = cv2.imread(path)
        assert img is not None, "Image could not be loaded."
        print(f"The shape of the image is: {img.shape}")
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        print(rgb)
        return rgb
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    except PermissionError as e:
        print(f"PermissionError: {e}")
    except OSError as e:
        print(f"OSError: {e}")


def main():
    """Main function to test the ft_load function."""
    ft_load('landscape.png')
    ft_load(5)
    ft_load('epacsdnal.jpg')
    ft_load('')


if __name__ == "__main__":
    main()
