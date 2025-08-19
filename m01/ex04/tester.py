from load_image import ft_load
from rotate import rimg


def main():
    """Main function to test the cut and transpose functions."""
    try:
        img = ft_load('animal.jpeg')
        rimg(img)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
