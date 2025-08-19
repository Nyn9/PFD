from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
from pimp_image import ft_grey
import numpy as np
import matplotlib.pyplot as plt


def display(img: np.ndarray):
    """Display an image with X/Y scale."""
    plt.imshow(img, cmap='gray')
    try:
        plt.show()
    except KeyboardInterrupt:
        plt.close()


def main():
    """Main function to test the cut and transpose functions."""
    try:
        img = ft_load("landscape.jpg")

        invert = ft_invert(img)
        red = ft_red(img)
        green = ft_green(img)
        blue = ft_blue(img)
        grey = ft_grey(img)

        print(ft_invert.__doc__)

        display(img)
        display(invert)
        display(red)
        display(green)
        display(blue)
        display(grey)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
