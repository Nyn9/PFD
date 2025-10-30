import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def zooom(pixels: np.array):
    """Zoom into the image pixels."""
    try:
        assert isinstance(pixels, np.ndarray), "Pixels must be a numpy array."
        start_y = 100
        start_x = 450
        size = 400
        zoom = pixels[start_y:start_y + size, start_x:start_x + size, 0:1]
        print(f"New shape after slicing: {zoom.shape} \
or {zoom.squeeze().shape}")
        print(zoom)
        plt.imshow(zoom, cmap='gray')
        plt.show()
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except KeyboardInterrupt:
        plt.close()


def main():
    """Main function to test the zoom function."""
    zooom(ft_load('animal.jpeg'))


if __name__ == "__main__":
    main()
