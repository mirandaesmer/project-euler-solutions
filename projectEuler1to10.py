from functools import reduce
from math import sqrt
from typing import List
from eulerPrimes import gen_primes, gen_ith_prime


class ProjectEuler1to10:
    def problem1(self) -> int:
        # If we list all the natural numbers below 10 that are multiples of 3 or
        # 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. # Find the
        # sum of all the multiples of 3 or 5 below 1000.
        return sum([n for n in range(1000) if (n % 3 == 0) or (n % 5 == 0)])
    
    def _problem2(self, n: int, _sum: int, mem: List[int]) -> int:
        term = mem[n - 1] + mem[n - 2]
        mem[n] = term
        
        if term >= 4000000:
            return _sum
        if term % 2 == 0:
            _sum += term
        return self._problem2(n + 1, _sum, mem)
    
    def problem2(self) -> int:
        # Each new term in the Fibonacci sequence is generated by adding the
        # previous two terms. By starting with [1, 2] the first 10 terms will be
        #     1, 2, 3, 5, 8, 13, 21, 34, 55, 89
        # By considering the terms in the Fibonacci sequence whose values do not
        # exceed four million, find the sum of the even-valued terms.
        mem = [1,2] + ([0] * 100)
        return self._problem2(2, 2, mem)
    
    def problem3(self) -> float:
        # The prime factors of 13195 are 5, 7, 13 and 29
        # What is the largest prime factor of the number 600851475143?
        number = 600851475143
        limit = int(sqrt(number))
        primes_upto = gen_primes(limit)
        
        for prime in primes_upto[::-1]:
            if 600851475143 % prime == 0:
                return prime
        return 0
    
    def _is_palindrome_fast(self, num: int) -> bool:
        # find if 5 or 6 digit:
        digits = 6 if num > 99999 else 5
        digit_list = [(num // (10 ** (i - 1))) % 10 for i in range(digits, 0, -1)]
        return digit_list == digit_list[::-1]
    
    def problem4(self) -> int:
        # A palindromic number reads the same both ways. The largest palindrome
        # made from the product of two 2-digit numbers is 9009 = 91 * 99. Find
        # the largest palindrome made from the product of two 3-digit numbers.
        max_palindrome = 0
        for i in range(999, 99, -1):
            for j in range(999, 99, -1):
                if self._is_palindrome_fast(i * j):
                    max_palindrome = max(max_palindrome, i * j)
        return max_palindrome  # Could be made more efficient
    
    def _is_20_div(self, num) -> int:
        for i in range(19, 1, -1):
            if num % i != 0:
                return False
        return True

    def problem5(self) -> int:
        # 2520 is the smallest number that can be divided by each of the numbers
        # from 1 to 10 without any remainder. What is the smallest positive
        # number that is evenly divisible (divisible with no remainder by all of
        # the numbers from 1 to 20)
        for candidate in range(20, 2000000000, 20):
            if self._is_20_div(candidate):
                return candidate
        return 0
        
    def problem6(self) -> int:
        # The sum of the squares of the first ten natural numbers is:
        #     1^2 + 2^2 + ... + 10^2 = 385
        # The square of the sum of the first ten natural numbers is,
        #     (1 + 2 + ... + 10)^2 = 55^2 = 3025
        # Hence the difference between the sum of the squares of the first ten
        # natural numbers and the square of the sum is
        #     3025 - 385 = 2640
        # Find the difference between the sum of the squares of the first one
        # hundred natural numbers and the square of the sum.
        sum_squares = sum([i ** 2 for i in range(1, 101)])
        squares_sum = sum(list(range(1, 101))) ** 2
        return squares_sum - sum_squares

    def problem7(self) -> int:
        # By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
        # can see that the 6th prime is 13. What is the 10001st prime number?
        return gen_ith_prime(10001)

    def problem8(self) -> int:
        # The four adjacent digits in the 1000-digit number below that have the
        # greatest product are 9 * 9 * 8 * 9 = 5832. <p>Find the thirteen
        # adjacent digits in the 1000-digit number that have the greatest
        # product. What is the value of this product?
        num_string = """
        73167176531330624919225119674426574742355349194934969835203127745063262
        39578318016984801869478851843858615607891129494954595017379583319528532
        08805511125406987471585238630507156932909632952274430435576689664895044
        52445231617318564030987111217223831136222989342338030813533627661428280
        64444866452387493035890729629049156044077239071381051585930796086670172
        42712188399879790879227492190169972088809377665727333001053367881220235
        42180975125454059475224352584907711670556013604839586446706324415722155
        39753697817977846174064955149290862569321978468622482839722413756570560
        57490261407972968652414535100474821663704844031998900088952434506585412
        27588666881164271714799244429282308634656748139191231628245861786645835
        91245665294765456828489128831426076900422421902267105562632111110937054
        42175069416589604080719840385096245544436298123098787992724428490918884
        58015616609791913387549920052406368991256071760605886116467109405077541
        00225698315520005593572972571636269561882670428252483600823257530420752
        963450"""
        
        for d in ['\n', '\t', ' ', '',]:
            num_string = num_string.replace(d, '')
        
        _max = 0
        for i in range(0, 1000 - 13):
            slice = [int(i) for i in num_string[i:i + 13]]
            if all(slice):  # contains no 0s
                product = reduce(lambda x, y: x * y, slice)
                _max = max(_max, product)
        return _max
    
    def problem9(self) -> int:
        # A Pythagorean triplet is a set of three natural numbers
        #     a < b < c for which a^2 + b^2 = c^2
        # For example
        #     3^2 + 4^2 = 9 + 16 = 25 = 5^2
        # There exists exactly one Pythagorean triplet for which
        #     a + b + c = 1000
        # Find the product a * b * c
        for a in range(1, 250):
            for b in range(a + 1, ((1000 - a) // 2) + a):  # limit search space
                c = 1000 - a - b
                if c != a and c != b and ((a ** 2) + (b ** 2) == c ** 2):
                    return a * b * c
        return 0

    def problem10(self) -> int:
        # The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
        # Find the sum of all the primes below two million.
        return sum(gen_primes(2000000))


if __name__ == "__main__":
    euler = ProjectEuler1to10()
    
    # print(euler.problem1())  # solved
    # print(euler.problem2())  # solved
    # print(euler.problem3())  # solved
    # print(euler.problem4())  # solved
    # print(euler.problem5())  # solved
    # print(euler.problem6())  # solved
    # print(euler.problem7())  # solved
    # print(euler.problem8())  # solved
    # print(euler.problem9())  # solved
    # print(euler.problem10())  # solved
