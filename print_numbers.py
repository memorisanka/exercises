"""User's input f.ex. 5
will give result:
1
22
333
4444
55555"""


def print_numbers():
    number = input("Enter number: ")

    for i in range(1, int(number) + 1):
        print(f"{str(i) * i}")


print_numbers()
