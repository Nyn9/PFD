import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def display(img: np.ndarray):
    """Display an image with X/Y scale."""
    plt.imshow(img, cmap='gray')
    try:
        plt.show()
    except KeyboardInterrupt:
        plt.close()


def tr(pixels: np.ndarray) -> np.ndarray:
    """Transpose an image to its rotated version."""
    if not isinstance(pixels, np.ndarray):
        raise AssertionError("Image pixels cannot be loaded.")
    h, w = pixels.shape
    result = np.zeros((w, h), dtype=pixels.dtype)
    for i in range(h):
        for j in range(w):
            result[j, i] = pixels[i, j]
    print("New shape after Transpose:", result.shape)
    print(result)
    return result


def cut(pixels: np.ndarray) -> np.ndarray:
    """Cut a square from the image."""
    if not isinstance(pixels, np.ndarray):
        raise AssertionError("Image pixels cannot be loaded.")
    size = 400
    start_y = 100
    start_x = 450
    cropped = pixels[start_y:start_y + size, start_x:start_x + size]

    cropped_expanded = cropped[:, :, np.newaxis]
    print("The shape of image is:", cropped_expanded.shape,
          "or", cropped_expanded.squeeze().shape)
    print(cropped_expanded)

    return cropped


def rimg(img: np.ndarray):
    """Rotate the image."""
    if not isinstance(img, np.ndarray):
        raise AssertionError("Image pixels cannot be loaded.")
    display(tr(cut(img)))


def main():
    """Main function to test the cut and transpose functions."""
    try:
        img = None
        rimg(img)
    except Exception as e:
        print(f"Error: {e}")

    try:
        img = ft_load('animal.jpeg')
        rimg(img)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
