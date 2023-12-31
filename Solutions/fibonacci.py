"""
Build the Fibonacci Sequence but with given inputs instead of set inputs, 0 and 1. Construct an additive sequence with t, a number of times to loop, a, a first starting digit, and b, a second starting digit.
Input
An integer t for the number of times to loop
An integer a as the first starting digit
An integer b as the second starting digit
Output
Line 1: a as it is at the start of the current loop
Line 2: a as it is at the start of the current loop
...
Line t: a as it is at the start of the current loop
Constraints
0<t≤75
0≤a≤25
0≤b≤500
Example
Input
10
0
1
Output
0
1
1
2
3
5
8
13
21
34
"""
import sys
import math

t = int(input())
a = int(input())
b = int(input())

prev = a
curr = b

print(prev)

for i in range(2, t+1):
    next_term = prev + curr
    print(curr)
    prev = curr
    curr = next_term
