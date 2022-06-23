# Description:
#
# This time no story, no theory. The examples below show you how to write function accum:
# Examples:
#
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
#
# The parameter of accum is a string which includes only letters from a..z and A..Z.


def accum(s: str) -> str:
    text = []
    idx = 1

    while idx < len(s) - 1:
        for letter in s:
            text.append((letter * idx).title())
            idx += 1

    return "-".join(text)


def main():
    print(accum("abcd"))
    print(accum("RqaEzty"))


if __name__ == "__main__":
    main()
