import sys


def main():
    av = sys.argv
    try:
        ac = len(av)
        assert ac <= 2, "more than one argument is provided"
        tmp = av[1].lstrip('-')
        assert tmp.isdigit(), "argument is not an integer"
        n = int(av[1])
        if n % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
    except IndexError as e:
        print(f"IndexError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
