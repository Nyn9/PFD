from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm


def main():
    """Tester for the custom progress bar."""

    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    print()

    for elem in tqdm(range(333)):
        sleep(0.005)
    print()


if __name__ == "__main__":
    main()
