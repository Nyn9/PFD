import sys


def main():
    av = sys.argv
    ac = len(av)
    if ac < 2:
        return
    try:
        assert ac <= 2, "more than one argument is provided"
        assert av[1].isdigit() or av[1].startswith('-'), "argument is not an integer"
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
