import sys


def main():
    av = sys.argv
    ac = len(av)
    if ac < 2:
        return
    try:
        if ac > 2:
            raise AssertionError("more than one argument is provided")
        if not av[1].isdigit() and not av[1].startswith('-'):
            raise AssertionError("argument is not an integer")
        n = int(av[1])
        if n % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
