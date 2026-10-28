import re


def is_palindrome(text: str) -> bool:
    left = 0
    right = len(text) - 1

    while left < right:
        if not re.fullmatch(r"[a-z0-9]", text[left], re.IGNORECASE):
            left += 1
            continue

        if not re.fullmatch(r"[a-z0-9]", text[right], re.IGNORECASE):
            right -= 1
            continue

        if text[left].lower() != text[right].lower():
            return False

        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    print(is_palindrome("racecar"))                       # True
    print(is_palindrome("Racecar"))                       # True
    print(is_palindrome("A man, a plan, a canal: Panama")) # True
    print(is_palindrome("race a car"))                    # False
    print(is_palindrome(""))                              # True
    print(is_palindrome("!!!"))                           # True
    print(is_palindrome("0P"))                            # False
