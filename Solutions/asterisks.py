"""
You must print the string A surrounded by asterisks to form a box.
Input
A The string
Output
Line 1 Length of A+4 stars
Line 2 A star followed by a space, then the string, another space and a final star.
Line 3 Length of A+4 stars
Constraints
Length of A < 64
Example
Input
Hello world!
Output
****************
* Hello world! *
****************
"""

# Read input values and convert them to integers
t, c, r = map(int, input().split())

# Calculate the maximum fuel that can be pumped within the given time
max_fuel = t * r

# Check if the maximum fuel is greater than or equal to the tank capacity
if max_fuel >= c:
    print("yes")  # The tank can be filled up within the time allowed
else:
    print("no")  # The tank cannot be filled up within the time allowed
