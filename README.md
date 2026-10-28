# Python Algorithms Lab

Python 3.10+ port of `ts-testing-lab.zip`. Each JavaScript algorithm is now a standalone
Python script in `src/`, with the same examples and iterative approach.

## Run an algorithm

From the project root:

```bash
python3 src/product_except_self.py
python3 src/missing_number.py
python3 src/is_palindrome.py
python3 src/longest_palindrome.py
python3 src/rob_rooms.py
```

## Run all tests

```bash
python3 -m unittest discover -s tests -v
```

No third-party dependencies required. The Jest `SpellBook` tests were ported
to Python's standard-library `unittest`.

## Files

| JavaScript / TypeScript source | Python port |
| --- | --- |
| `isPalindrome.js` | `src/is_palindrome.py` |
| `longetsPlaindrome.js` (original filename typo) | `src/longest_palindrome.py` |
| `missingNumber.js` | `src/missing_number.py` |
| `productExceptSelf.js` | `src/product_except_self.py` |
| `robRooms.js` | `src/rob_rooms.py` |
| `SpellBook.ts` | `src/spell_book.py` |
| `SpellBook.spec.ts` | `tests/test_spell_book.py` |

### Python differences to notice

- `range(len(nums) - 1, -1, -1)` iterates backward, including index 0.
- `text[left + 1:right]` is Python slicing; end is exclusive.
- `sum(nums)` replaces JavaScript's `reduce` for summing.
- `//` is integer division, used in the missing-number formula.
- Python `int` has arbitrary precision; multiplying integer zero yields `0`,
  not JavaScript floating-point `-0`.
- Python names conventionally use `snake_case`.
- `if __name__ == "__main__":` runs examples only when the file is executed
  directly, not when imported by tests.
# python-algorithms-lab
