def missing_number(nums: list[int]) -> int:
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


if __name__ == "__main__":
    print(missing_number([3, 0, 1]))                   # 2
    print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1])) # 8
    print(missing_number([0, 1]))                      # 2
    print(missing_number([1]))                         # 0
    print(missing_number([0]))                         # 1
    print(missing_number([0, 1, 2, 3, 4]))             # 5
    print(missing_number([]))                          # 0
