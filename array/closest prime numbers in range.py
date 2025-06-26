"""
Closest Prime Numbers in Range
Given two positive integers left and right, find the two integers num1 and num2 such that:

left <= num1 < num2 <= right .
Both num1 and num2 are prime numbers.
num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these 
conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

 

Example 1:

Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.
Example 2:

Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the conditions cannot be 
satisfied.

Solution:
In this approach, we take advantage of a special property of prime numbers known as twin primes, which 
are pairs of prime numbers that differ by exactly 2, such as (3,5), (11,13), and (17,19). Instead of 
searching through all prime numbers, we can optimize our search by focusing on this pattern.
A key known mathematical observation is that for any range [L, R] where R - L ≥ 1452, there is always 
at least one twin prime pair. This means that if the given range is wide enough (at least 1452 numbers
long), we can be certain that a twin prime pair exists. Since no two prime numbers can be closer than 
a twin prime pair (which has a difference of exactly 2), we can immediately return this result without 
further searching.

However, if the range [L, R] is smaller than 1452 numbers, we cannot rely on this property and must 
manually find the closest prime pair. To do this, we iterate through the numbers in the range, check 
which ones are prime, and compute the smallest difference between consecutive primes.

Since twin primes are common, this approach is much faster in practice than scanning all numbers in 
[L,R].

Algorithm
Main Function: closestPrimes(int left, int right)

Initialize Variables:

primeNumbers: A list to store prime numbers found within the range [left, right].
Find All Prime Numbers in Range [left, right]:

Iterate through all numbers from left to right:
Skip even numbers greater than 2 since they are not prime.
Use isPrime(candidate) to check if the number is prime.
If the number is prime:
If the last stored prime and the current number form a twin prime (difference ≤ 2), return the pair 
immediately.
Otherwise, store the prime number in primeNumbers.
Handle Cases with Fewer Than 2 Primes:

If primeNumbers contains fewer than 2 elements, return {-1, -1}.
Find the Closest Prime Pair:

Initialize closestPair = {-1, -1} and minDifference = 1e6 (large value).
Iterate through primeNumbers, calculating the difference between consecutive primes.
Update closestPair whenever a smaller difference is found.
Return Result:

Return closestPair, which contains the closest pair of primes.
Helper Function: isPrime(int number)

Check for Edge Case:

If number == 1, return false (1 is not prime).
Check for Divisibility:

Iterate from 2 to sqrt(number).
If number is divisible by any of these, return false.
Return True if Prime:

If no divisors are found, return true.
"""

def is_prime(num):
    if num == 1:
        return False
    for divisor in range(2, int(num**0.5)+1):
        print(num)
        if num % divisor == 0:
            return False
    return True

def sieve(upper_limit):
    """
    FYI (Not used in this approach)
    A much faster way to find all prime numbers up to a given limit is the Sieve of Eratosthenes. 
    Instead of checking each number one by one, the sieve marks multiples of each prime in bulk, 
    eliminating the need for repeated divisibility checks.

    We start with a list of numbers from 2 to 100. Notice we skip 1 since it’s not considered a prime. 
    Starting with the smallest prime, 2, we know it’s prime because it hasn’t been marked yet. So, we 
    keep it. Now, we cross out all multiples of 2 (like 4, 6, 8, etc.) because they’re definitely not 
    prime. The next number that isn’t crossed out is 3, so we mark it as a prime. Then, we cross out 
    all multiples of 3 (like 6, 9, 12, etc.). We keep going, finding the next unmarked number 
    (which will be 5), and marking all of its multiples. We do this for 7 as well and continue until 
    we’ve processed all numbers up to the limit.
    """
    sieve_arr = [True]*(upper_limit + 1)
    sieve_arr[0] = sieve_arr[1] = False

    for num in range(2, int(upper_limit ** 0.5) + 1):
        if sieve_arr[num]:
            for multiple in range(num*num, upper_limit + 1, num):
                sieve_arr[multiple] = False
    return sieve_arr

def closestPrimes(left, right):
    prime_list = []

    for num in range(left, right+1):
        if num % 2==0 and num > 2:
            continue
        if is_prime(num):
            if prime_list and num <= prime_list[-1] + 2:
                return [prime_list[-1], num]
            prime_list.append(num)

    pair = [-1,-1]
    if len(prime_list) < 2:
        return pair
    min_diff = 1e6
    for index in range(1, len(prime_list)):
        diff = prime_list[index] - prime_list[index-1]
        if diff < min_diff:
            min_diff = diff
            pair = [prime_list[index-1], prime_list[index]]
    return pair

