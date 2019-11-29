error = "please enter a natural number n<27 and try again..."

try:
    n = int(input())
    assert 0 < 20
except(ValueError, AssertionError):
    print(error)
    exit()
from string import ascii_lowercase

width = 4*n - 3
s = ascii_lowercase[:n]
s = s[::-1] + s[1:]

for c in s:
    pattern = s[:s.index(c)]
    pattern = '-'.join(pattern + c + pattern[::-1])
    dashes = (width - len(pattern)) // 2 * '-'
    print(dashes + pattern + dashes)
