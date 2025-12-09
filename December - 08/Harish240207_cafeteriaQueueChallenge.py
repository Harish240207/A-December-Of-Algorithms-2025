# December 08 - Cafeteria Queue Challenge

def students_unable_to_eat(students, sandwiches):
    # Count how many students prefer 0 or 1
    count_pref = {0: 0, 1: 0}
    for s in students:
        count_pref[s] += 1

    # Try to serve sandwiches one by one
    for sand in sandwiches:
        # If no student wants this type, remaining cannot eat
        if count_pref[sand] == 0:
            return count_pref[0] + count_pref[1]

        # Otherwise, serve one student of this type
        count_pref[sand] -= 1

    # If all sandwiches were served
    return 0


def main():
    # Read inputs
    n = int(input().strip())
    students = list(map(int, input().split()))
    sandwiches = list(map(int, input().split()))

    # Use only first n elements if extra provided
    students = students[:n]
    sandwiches = sandwiches[:n]

    print(students_unable_to_eat(students, sandwiches))


if __name__ == "__main__":
    main()
