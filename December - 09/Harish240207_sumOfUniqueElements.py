# December 09 - Sum of Unique Elements

def sum_of_unique(arr):
    freq = {}

    # Count occurrences
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    # Sum only elements with frequency == 1
    total = sum(num for num, count in freq.items() if count == 1)
    return total


def main():
    n = int(input().strip())
    arr = list(map(int, input().split()))
    arr = arr[:n]
    
    print(sum_of_unique(arr))


if __name__ == "__main__":
    main()
