import sys
from ft_filter import ft_filter


def main():
    """Prints words longer than a specified length from a string."""
    av = sys.argv
    ac = len(av)
    try:
        if ac != 3:
            raise AssertionError("the arguments are bad")
        if (not av[1] or (not av[1].isalpha() and av[1].isspace()) or not av[2].isdigit()):
            raise AssertionError("the arguments are bad")
        s = av[1].split(' ')
        length = int(av[2])
        word = [w for w in s if w.isalpha()]
        print(list(ft_filter(lambda x: len(x) > length, word)))
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
