# December 07 - Baseball Score Record Keeper
# Input:
#   Line 1: integer N (number of operations)
#   Line 2: N space-separated strings (each is "C", "D", "+", or an integer string)
#
# Output:
#   Single integer: total sum of scores after all operations

def compute_score(ops):
    scores = []

    for op in ops:
        if op == "C":
            # Remove the last valid score
            scores.pop()
        elif op == "D":
            # Double the last valid score
            scores.append(2 * scores[-1])
        elif op == "+":
            # Sum of last two valid scores
            scores.append(scores[-1] + scores[-2])
        else:
            # Integer score
            scores.append(int(op))

    return sum(scores)


def main():
    # Read N
    N = int(input().strip())

    # Read operations as strings
    ops = input().split()
    # In case there are extra tokens, keep only N
    ops = ops[:N]

    total = compute_score(ops)
    print(total)


if __name__ == "__main__":
    main()