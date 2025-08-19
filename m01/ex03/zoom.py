import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def display(img: np.ndarray):
    """Display an image with X/Y scale."""
    plt.imshow(img, cmap='gray')
    plt.xlabel("X axis (pixels)")
    plt.ylabel("Y axis (pixels)")
    try:
        plt.show()
    except KeyboardInterrupt:
        plt.close()


def zooom(pixels: np.array, size: int):
    """Zoom into the image pixels."""
    if not isinstance(pixels, np.ndarray):
        raise AssertionError("Image pixels cannot be loaded.")
    if not isinstance(size, int) or size <= 0:
        raise AssertionError("Size must be a positive integer.")
    h, w, _ = pixels.shape
    start_y = h // 2 - size // 2
    start_x = w // 2 - size // 2
    zoom = pixels[start_y:start_y + size, start_x:start_x + size, 0:1]
    print(f"New shape after slicing: {zoom.shape} or {zoom.squeeze().shape}")
    print(zoom)
    display(zoom)


def main():
    """Main function to test the zoom function."""
    try:
        zooom(None, 400)
    except Exception as e:
        print(f"Error: {e}")

    try:
        img = ft_load('animal.jpeg')
        zooom(img, -400)
    except Exception as e:
        print(f"Error: {e}")

    try:
        zooom("img", 400)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
