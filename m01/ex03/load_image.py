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
    img = cv2.imread(path)
    if img is None:
        raise AssertionError("Image could not be loaded.")
    print(f"The shape of the image is: {img.shape}")
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    print(rgb)
    return rgb
