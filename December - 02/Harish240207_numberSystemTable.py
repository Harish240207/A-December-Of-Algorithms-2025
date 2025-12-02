# December 02 - Total of Distinct Values (Number System Table)
# Reads an integer N and prints numbers from 1 to N in
# decimal, octal, hexadecimal (uppercase), and binary, in aligned columns.

def main():
    # Read input
    N = int(input().strip())

    # Width of the columns = length of binary of N
    width = len(bin(N)) - 2  # subtract 2 to ignore '0b'

    for i in range(1, N + 1):
        dec_str = str(i).rjust(width)
        oct_str = oct(i)[2:].rjust(width)          # remove '0o'
        hex_str = hex(i)[2:].upper().rjust(width)  # remove '0x' and uppercase
        bin_str = bin(i)[2:].rjust(width)          # remove '0b'

        # Print the four columns on one line
        print(dec_str, oct_str, hex_str, bin_str)


if __name__ == "__main__":
    main()
