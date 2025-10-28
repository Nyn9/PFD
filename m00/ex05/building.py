import sys


def main():
    """Count types of characters in a string"""
    av = sys.argv
    ac = len(av)

    try:
        assert ac <= 2, "more than one argument is provided"
        if ac < 2:
            print("What is the text to count?", flush=True)
            s = sys.stdin.readline()
        else:
            s = av[1]
        print(f"The text contains {len(s)} characters:")
        print(f"{sum(1 for c in s if c.isupper())} upper letters")
        print(f"{sum(1 for c in s if c.islower())} lower letters")
        print(f"{sum(1 for c in s if not c.isalnum() and not c.isspace())} \
punctuation marks")
        print(f"{sum(1 for c in s if c.isspace())} spaces")
        print(f"{sum(1 for c in s if c.isdigit())} digits")
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
