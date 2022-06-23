# Description:
#
# Make a program that filters a list of strings and returns a list with only your friends name in it.
#
# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours!
# Otherwise, you can be sure he's not...
#
# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]


def friend(fr: list) -> list:
    return [name for name in fr if len(name) == 4]


def main():
    print(friend(["Ryan", "Kieran", "Mark"]))


if __name__ == "__main__":
    main()
