import numpy as np
import matplotlib.pyplot as plt


def display(img: np.ndarray):
    """Display an image with X/Y scale."""
    try:
        plt.imshow(img, cmap='gray')
        plt.show()
    except KeyboardInterrupt:
        plt.close()

def ft_invert(array) -> np.ndarray:
    """Inverse all colors"""
    try:
        assert isinstance(array, np.ndarray), "Input must be a numpy array."
        assert array.ndim == 3 and array.shape[2] == 3, \
            "Input must be a 3-channel RGB image."
        new = 255 - array
        display(new)
        return new
    except AssertionError as e:
        print(f"AssertionError: {e}")


def ft_red(array) -> np.ndarray:
    """Keep only red channel"""
    try:
        assert isinstance(array, np.ndarray), "Input must be a numpy array."
        assert array.ndim == 3 and array.shape[2] == 3, \
            "Input must be a 3-channel RGB image."
        new = array * [1, 0, 0]
        display(new)
        return new
    except AssertionError as e:
        print(f"AssertionError: {e}")


def ft_green(array) -> np.ndarray:
    """Keep only green channel"""
    try:
        assert isinstance(array, np.ndarray), "Input must be a numpy array."
        assert array.ndim == 3 and array.shape[2] == 3, \
            "Input must be a 3-channel RGB image."
        result = array.copy()
        result[:, :, 0] -= result[:, :, 0]
        result[:, :, 2] -= result[:, :, 2]
        display(result)
        return result
    except AssertionError as e:
        print(f"AssertionError: {e}")


def ft_blue(array) -> np.ndarray:
    """Keep only blue channel"""
    try:
        assert isinstance(array, np.ndarray), "Input must be a numpy array."
        assert array.ndim == 3 and array.shape[2] == 3, \
            "Input must be a 3-channel RGB image."
        result = array.copy()
        result[:, :, 0] = 0
        result[:, :, 1] = 0
        display(result)
        return result
    except AssertionError as e:
        print(f"AssertionError: {e}")


def ft_grey(array) -> np.ndarray:
    """Convert to grey"""
    try:
        assert isinstance(array, np.ndarray), "Input must be a numpy array."
        assert array.ndim == 3 and array.shape[2] == 3, \
            "Input must be a 3-channel RGB image."
        grey = array[:, :, 1]
        result = np.zeros_like(array)
        result[:, :, 0] = grey
        result[:, :, 1] = grey
        result[:, :, 2] = grey
        display(result)
        return result
    except AssertionError as e:
        print(f"AssertionError: {e}")


def main():
    """Main function to test the image processing functions."""

    ft_invert(None)

    arr = np.array([0, 1])
    ft_invert(arr)


if __name__ == "__main__":
    main()
