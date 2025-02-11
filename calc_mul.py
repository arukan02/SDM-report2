#!/usr/bin/python3

import re
                
def calc(A, B):
    # Check if A and B are integers
    if not isinstance(A, int) or not isinstance(B, int):
        return -1

    # Check valid range (1 <= A, B <= 999)
    if 1 <= A <= 999 and 1 <= B <= 999:
        return A * B
    else:
        return -1

def main():
    while True:
        try:
            A = input('input A: ')
            B = input('input B: ')

            if A.lower() == 'end' or B.lower() == 'end':
                break

            # Convert input to integer
            A = int(A)
            B = int(B)

            print('input A * input B =', calc(A, B))

        except ValueError:
            print("Invalid input. Please enter integers between 1 and 999.")

if __name__ == '__main__':
    main()
