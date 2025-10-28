import sys
from ft_filter import ft_filter


def main():
    """Prints words longer than a specified length from a string."""
    av = sys.argv
    ac = len(av)
    try:
        assert ac == 3, "the arguments are bad"
        assert av[1] and (av[1].isalpha() or av[1].isspace()) and av[2].isdigit(), "the arguments are bad"
        s = av[1].split(' ')
        length = int(av[2])
        word = [w for w in s if w.isalpha()]
        print(list(ft_filter(lambda x: len(x) > length, word)))
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
