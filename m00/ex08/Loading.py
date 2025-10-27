import os


def ft_tqdm(lst: range) -> None:
    """Custom progress bar similar to tqdm."""
    total = len(lst)
    size = os.get_terminal_size().columns - 40
    for i, item in enumerate(lst):
        percent = int((i + 1) / total * 100)
        bar = ('█' * (int((percent / 100) * size))).ljust(size)
        print(f"\r{percent}%|{bar}| {i + 1}/{total}", end="")
        yield item
    print()


from time import sleep

def main():
    """Tester for the custom progress bar."""
    for elem in ft_tqdm(range(10)):
        sleep(0.01)
    print()


if __name__ == "__main__":
    main()
