def can_reach_last(stones):
    n = len(stones)
    last_index = n - 1
    farthest = 0

    for i, jump in enumerate(stones):
        if i > farthest:
            return False

        farthest = max(farthest, i + jump)

        if farthest >= last_index:
            return True

    return farthest >= last_index


def main():
    stones = list(map(int, input().split()))

    if can_reach_last(stones):
        print("true")
    else:
        print("false")


if __name__ == "__main__":
    main()
