# December 06 - Magic Square of Odd Order
# Input:
#   Single integer n (order of the magic square)
#
# Output:
#   If n is even:
#       Magic square is only possible for odd values of n.
#   If n is odd:
#       Magic constant: M
#       <n x n magic square grid>

def generate_magic_square(n):
    # Create an n x n matrix filled with 0
    magic = [[0] * n for _ in range(n)]

    # Siamese method
    num = 1
    row, col = 0, n // 2  # start at middle of top row

    while num <= n * n:
        magic[row][col] = num

        # Save current position before moving
        prev_row, prev_col = row, col

        # Move up-right
        row = (row - 1) % n
        col = (col + 1) % n

        # If the next cell is already filled, move down from the previous cell
        if magic[row][col] != 0:
            row = (prev_row + 1) % n
            col = prev_col

        num += 1

    return magic


def main():
    # Read n
    n = int(input().strip())

    # Check if n is odd
    if n % 2 == 0:
        print("Magic square is only possible for odd values of n.")
        return

    # Compute magic constant
    M = n * (n * n + 1) // 2
    print(f"Magic constant: {M}")

    # Generate the magic square
    magic = generate_magic_square(n)

    # Print the magic square grid
    for row in magic:
        # Print numbers space-separated
        print(" ".join(str(x) for x in row))


if __name__ == "__main__":
    main()
