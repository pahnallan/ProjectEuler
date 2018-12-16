# Problem 3
# Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
# Key requirements here are: What is the definition of a prime factor? How do you determine if a number is prime


NUMBER = 600851475143
ANSWER = 6857


def main():
    assert solution_1() == ANSWER


def solution_1():
    number = NUMBER
    factor = 2
    while factor < number:
        if number % factor == 0:
            number = number / factor
        else:
            factor += 1
    return factor


if __name__ == "__main__":
    main()
