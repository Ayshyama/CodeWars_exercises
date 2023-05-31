"""
Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.

Example:
h = 0
m = 1
s = 1

result = 61000
Input constraints:

0 <= h <= 23
0 <= m <= 59
0 <= s <= 59
"""


def milliseconds_since_midnight(hours, minutes, seconds):
    if 0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59:
        return (hours * 3600 + minutes * 60 + seconds) * 1000
    else:
        return 'Invalid input'


def past(hours, minutes, seconds):
    return (3600*hours + 60*minutes + seconds) * 1000


h = 0
m = 10
s = 1
result = past(h, m, s)
print(result)