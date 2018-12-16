# Problem 1
# Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
# multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

UPPER_LIMIT = 1000
ANSWER = 233168


def main():
    print("Starting test.")
    assert solution_1() == ANSWER
    assert solution_2() == ANSWER
    print("Tests passed.")


def solution_1():
    sum_of_numbers = 0
    for index in range(UPPER_LIMIT):
        if index % 3 == 0 or index % 5 == 0:
            sum_of_numbers += index
    return sum_of_numbers


def solution_2():
    return sum(index for index in range(UPPER_LIMIT) if index % 3 == 0 or index % 5 == 0)


if __name__ == "__main__":
    main()
