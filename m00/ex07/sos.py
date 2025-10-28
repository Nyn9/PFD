import sys


def translate_morse_char(c):
    """Translates a single character to Morse code.
    Raises AssertionError if the character is not valid.
    """
    morse_dict = {
                        " ": "/ ",
                        "A": ".- ",
                        "B": "-... ",
                        "C": "-.-. ",
                        "D": "-.. ",
                        "E": ". ",
                        "F": "..-. ",
                        "G": "--. ",
                        "H": ".... ",
                        "I": ".. ",
                        "J": ".--- ",
                        "K": "-.- ",
                        "L": ".-.. ",
                        "M": "-- ",
                        "N": "-. ",
                        "O": "--- ",
                        "P": ".--. ",
                        "Q": "--.- ",
                        "R": ".-. ",
                        "S": "... ",
                        "T": "- ",
                        "U": "..- ",
                        "V": "...- ",
                        "W": ".-- ",
                        "X": "-..- ",
                        "Y": "-.-- ",
                        "Z": "--.. ",
                        "0": "----- ",
                        "1": ".---- ",
                        "2": "..--- ",
                        "3": "...-- ",
                        "4": "....- ",
                        "5": "..... ",
                        "6": "-.... ",
                        "7": "--... ",
                        "8": "---.. ",
                        "9": "----. ",
                    }
    assert c.upper() in morse_dict, "the arguments are bad"
    return morse_dict[c.upper()]


def main():
    """Translate a string to Morse code."""
    av = sys.argv
    ac = len(av)
    try:
        assert ac == 2, "the arguments are bad"
        s = av[1]
        morse_code = ''.join(translate_morse_char(c) for c in s)
        print(morse_code.strip())
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
