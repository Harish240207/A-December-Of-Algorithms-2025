def find_target_subarray(arr, K):
    n = len(arr)
    prefix_index = {0: -1} 
    current_sum = 0

    for i in range(n):
        current_sum += arr[i]
        needed = current_sum - K

        if needed in prefix_index:
            start = prefix_index[needed] + 1
            end = i
            return start, end
        if current_sum not in prefix_index:
            prefix_index[current_sum] = i
    return -1, -1


def main():
    first_line = input().split()
    N = int(first_line[0])
    K = int(first_line[1])
    arr = list(map(int, input().split()))
    arr = arr[:N]

    start, end = find_target_subarray(arr, K)
    print(start, end)


if __name__ == "__main__":
    main()
