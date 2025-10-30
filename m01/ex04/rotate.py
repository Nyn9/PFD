import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def transpose(pixels: np.ndarray) -> np.ndarray:
    """Transpose an image to its rotated version."""
    try:
        assert isinstance(pixels, np.ndarray), "Pixels must be a numpy array."
        pixels = pixels[:, :, 0]
        h, w = pixels.shape
        result = np.zeros((w, h), dtype=pixels.dtype)
        for i in range(h):
            for j in range(w):
                result[j, i] = pixels[i, j]
        print("New shape after Transpose:", result.shape)
        print(result)
        plt.imshow(result, cmap='gray')
        plt.show()
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except KeyboardInterrupt:
        plt.close()


def cut(pixels: np.ndarray) -> np.ndarray:
    """Cut a square from the image."""
    try:
        assert isinstance(pixels, np.ndarray), "Pixels must be a numpy array."
        start_y = 100
        start_x = 450
        size = 400
        cropped = pixels[start_y:start_y + size, start_x:start_x + size]
        return cropped
    except AssertionError as e:
        print(f"AssertionError: {e}")


def main():
    """Main function to test the cut and transpose functions."""
    img = ft_load('animal.jpeg')
    cut_img = cut(img)
    transpose(cut_img)



if __name__ == "__main__":
    main()
