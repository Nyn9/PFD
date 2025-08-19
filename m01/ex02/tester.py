from load_image import ft_load


def main():
    """Main function to test the ft_load function."""
    try:
        ft_load("landscape.jpg")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
