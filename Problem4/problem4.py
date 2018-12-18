# Problem 4
# Largest palindrome product
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers.


POWER = 2
ANSWER = 906609


def main():
    assert solution_1() == ANSWER


def solution_1():
    start = 100
    end = 1000
    palindrome_high = 0
    for number in range(start, end):
        for second_number in range(number, end):
            prod = number*second_number
            if is_palindrom(prod) and prod > palindrome_high:
                palindrome_high = prod
    return palindrome_high


def is_palindrom(number):
    number_str = str(number)
    for index in range(len(number_str)//2):
        if number_str[index] != number_str[len(number_str)-index-1]:
            return False
    return True


if __name__ == "__main__":
    main()
