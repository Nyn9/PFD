from time import sleep
import os


def ft_tqdm(lst: range) -> None:
    """Custom progress bar similar to tqdm."""
    try:
        total = len(lst)
        size = os.get_terminal_size().columns - 40
    except OSError:
        size = 80
    except TypeError:
        print("TypeError: 'range' object is required.")
        return
    for i, item in enumerate(lst):
        percent = int((i + 1) / total * 100)
        bar = ('█' * (int((percent / 100) * size))).ljust(size)
        print(f"\r{percent}%|{bar}| {i + 1}/{total}", end="")
        yield item
    print()


def main():
    """Tester for the custom progress bar."""
    for elem in ft_tqdm("abc"):
        sleep(0.01)
    print()


if __name__ == "__main__":
    main()
