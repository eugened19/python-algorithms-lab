def product_except_self(nums: list[int]) -> list[int]:
    answer = [1] * len(nums)

    # WALK 1: Left → Right
    # Product of everything BEFORE the current element.
    for i in range(1, len(nums)):
        answer[i] = answer[i - 1] * nums[i - 1]

    # WALK 2: Right → Left
    # Product of everything AFTER the current element.
    right_product = 1

    for i in range(len(nums) - 1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]

    return answer


if __name__ == "__main__":
    print(product_except_self([1, 2, 3, 4]))       # [24, 12, 8, 6]
    print(product_except_self([-1, 1, 0, -3, 3])) # [0, 0, 9, 0, 0]
