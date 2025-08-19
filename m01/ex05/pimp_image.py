from load_image import ft_load
import numpy as np


def ft_invert(array) -> np.ndarray:
    """Inverse all colors"""
    if not isinstance(array, np.ndarray):
        raise AssertionError("Input must be a numpy array.")
    if array.ndim != 3 or array.shape[2] != 3:
        raise AssertionError("Input must be a 3-channel RGB image.")
    return 255 - array


def ft_red(array) -> np.ndarray:
    """Keep only red channel"""
    if not isinstance(array, np.ndarray):
        raise AssertionError("Input must be a numpy array.")
    if array.ndim != 3 or array.shape[2] != 3:
        raise AssertionError("Input must be a 3-channel RGB image.")
    return array * [1, 0, 0]


def ft_green(array) -> np.ndarray:
    """Keep only green channel"""
    if not isinstance(array, np.ndarray):
        raise AssertionError("Input must be a numpy array.")
    if array.ndim != 3 or array.shape[2] != 3:
        raise AssertionError("Input must be a 3-channel RGB image.")
    result = array.copy()
    result[:, :, 0] = result[:, :, 0] - result[:, :, 0]
    result[:, :, 2] = result[:, :, 2] - result[:, :, 2]
    return result


def ft_blue(array) -> np.ndarray:
    """Keep only blue channel"""
    if not isinstance(array, np.ndarray):
        raise AssertionError("Input must be a numpy array.")
    if array.ndim != 3 or array.shape[2] != 3:
        raise AssertionError("Input must be a 3-channel RGB image.")
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 1] = 0
    return result


def ft_grey(array) -> np.ndarray:
    """Convert to grey"""
    if not isinstance(array, np.ndarray):
        raise AssertionError("Input must be a numpy array.")
    if array.ndim != 3 or array.shape[2] != 3:
        raise AssertionError("Input must be a 3-channel RGB image.")
    grey = array[:, :, 1]
    result = np.zeros_like(array)
    result[:, :, 0] = grey
    result[:, :, 1] = grey
    result[:, :, 2] = grey
    return result


def main():
    """Main function to test the image processing functions."""

    try:
        invert = ft_invert(None)
    except Exception as e:
        print(f"Error: {e}")

    try:
        arr = np.array([0, 1])
        invert = ft_invert(arr)
    except Exception as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    main()
