# Description:
#
# Implement a function that accepts 3 integer values a, b, c. The function should
# return true if a triangle can be built with the sides of given length and false in any other case.
#
# (In this case, all triangles must have surface greater than 0 to be accepted).


def is_triangle(a, b, c) -> bool:
    if a + b > c and a + c > b and b + c > a:
        return True
    return False


def main():
    print(is_triangle(4, 5, 7))
    print(is_triangle(12, 10, 25))


if __name__ == "__main__":
    main()
