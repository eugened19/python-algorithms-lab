def rob(rooms: list[int]) -> int:
    two_rooms_back_best = 0
    previous_best = 0
    current_best = 0

    for current_room in rooms:
        skip = previous_best
        take = current_room + two_rooms_back_best

        current_best = max(skip, take)

        two_rooms_back_best = previous_best
        previous_best = current_best

    return current_best


if __name__ == "__main__":
    print(rob([5, 1, 1, 5]))    # 10
    print(rob([2, 7, 9, 3, 1])) # 12
    print(rob([1, 2, 3, 1]))    # 4
    print(rob([10]))           # 10
    print(rob([]))             # 0
