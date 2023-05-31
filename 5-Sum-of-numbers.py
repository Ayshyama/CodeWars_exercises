"""
Given two integers a and b, which can be positive or negative.
Find the sum of all the integers between and including them and return it.
If the two numbers are equal return a or b.

Note: a and b are not ordered!

Examples (a, b) --> output (explanation)
(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
Your function should only return a number, not the explanation about how you get that number.
"""


def get_sum(a, b):
    if a == b:
        return a
    else:
        return sum(range(min(a, b), max(a, b) + 1))


print(get_sum(1, 0))    # Output: 1
print(get_sum(1, 2))    # Output: 3
print(get_sum(0, 1))    # Output: 1
print(get_sum(1, 1))    # Output: 1
print(get_sum(-1, 0))   # Output: -1
print(get_sum(-1, 2))   # Output: 2
