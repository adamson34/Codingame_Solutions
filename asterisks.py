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

A = input()
length_A = len(A)

print('*' * (length_A + 4))
print('* ' + A + ' *')
print('*' * (length_A + 4))
