def expand_around_center(text: str, left: int, right: int) -> str:
    while (
        left >= 0
        and right < len(text)
        and text[left] == text[right]
    ):
        left -= 1
        right += 1

    return text[left + 1:right]


def find_longest_palindrome(text: str) -> str:
    longest_palindrome = ""

    for i in range(len(text)):
        current_palindrome = expand_around_center(text, i, i)

        if len(current_palindrome) > len(longest_palindrome):
            longest_palindrome = current_palindrome

        current_palindrome = expand_around_center(text, i, i + 1)

        if len(current_palindrome) > len(longest_palindrome):
            longest_palindrome = current_palindrome

    return longest_palindrome


if __name__ == "__main__":
    print(find_longest_palindrome("racecar"))  # racecar
    print(find_longest_palindrome("abba"))     # abba
    print(find_longest_palindrome("babad"))    # bab or aba
    print(find_longest_palindrome("cbbd"))     # bb
    print(find_longest_palindrome("abc"))      # a
    print(find_longest_palindrome("a"))        # a
    print(find_longest_palindrome(""))         # ""
