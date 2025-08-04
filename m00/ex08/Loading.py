from time import sleep


def ft_tqdm(lst: range) -> None:
    """Custom progress bar similar to tqdm."""
    total = len(lst)
    for i, item in enumerate(lst):
        percent = int((i + 1) / total * 100)
        bar = ('█' * ((percent // 2) + 5)).ljust(55)
        print(f"\r{percent}%|{bar}| {i + 1}/{total}", end="")
        yield item
    print()


def main():
    """Tester for the custom progress bar."""
    for elem in ft_tqdm(range(10)):
        sleep(0.01)
    print()


if __name__ == "__main__":
    main()
