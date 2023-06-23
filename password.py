"""

Björn owns a small company with 6 employees. He has decided to give a gift for the most secure password in the company, given the following rules:

A password s is valid only if:

- its length is 8 <= s <= 15
- it contains at least one number
- it contains at least one upper-case character
- it doesn't contain any space

He attributes points like this:

- each space char gives 0 point
- each upper-case char gives 10 points
- each lower-case char gives 5 points
- each number gives only 1 point
- every other char (like " ! . , & - @) gives 25 points.

For example, !Bash&234a.r, ====> returns True, 138 where 138 is the sum of the points of each char.
Input
Line 1: The password string s, which contains only ASCII characters.
Output
A string valid, points based on the given password, where:

- valid is True or False
- points is an integer that represents the sum of the points of each char in the password
Constraints
Example
Input
BigPassword
Output
False, 65

"""

s = input()
points = 0
has_number = False
has_uppercase = False
has_space = False

for c in s:
    if c.isspace():
        points += 0
        has_space = True
    elif c.isupper():
        points += 10
        has_uppercase = True
    elif c.islower():
        points += 5
    elif c.isdigit():
        points += 1
        has_number = True
    else:
        points += 25

valid = (
    8 <= len(s) <= 15
    and has_number
    and has_uppercase
    and not has_space
)

print(f"{valid}, {points}")
