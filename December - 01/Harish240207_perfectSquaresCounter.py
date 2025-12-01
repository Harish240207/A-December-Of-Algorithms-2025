# Perfect Squares Counter
# Reads an integer N, prints all perfect squares from 1 to N, then their count.

def main():
    # Read input
    N = int(input().strip())

    squares = []
    i = 1
    # While i^2 <= N, we have a valid perfect square
    while i * i <= N:
        squares.append(i * i)
        i += 1

    # Print squares in one line separated by space
    print(" ".join(map(str, squares)))
    # Print count in next line
    print(len(squares))


if __name__ == "__main__":
    main()
