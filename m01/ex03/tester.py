from load_image import ft_load
from zoom import zooom


def main():
    """Main function to test the zoom function."""
    img = ft_load("animal.jpeg")
    zooom(img, 400)


if __name__ == "__main__":
    main()
