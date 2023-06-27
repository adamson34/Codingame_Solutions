"""
Congrats! You are our new IT guy and your job is to see if the IP address is IPv4 or IPv6 or NONE. You have 15 minutes to make this program before your job starts and you surely don't want to do that manually. GLHF

You will get string input and based on that you will need to check if the address format is one of the following :

IPv4: 4 numbers who are less or equal 255 and higher than 0 and the format is following. ex. : 123.123.123.123 (Must not contain negative numbers in the address)

IPv6: 8 strings consisted of characters and numbers and the length of each part is exactly 4. ex. :
3001:0da8:75a3:0000:0000:8a2e:0370:7334. (Must not contain - (minus) in the address)

Keep in mind some IP addresses maybe are missing a character or two and letters could be mixed up with upper and lowercase letters
IPv6 can contain only A, B, C, D, E, F letters while IPv4 contains numbers only
Input
You input is string input stored in variable named address.
Output
Your output needs to be a string with the value IPv4 if the address is IPv4, IPv6 it the address is IPv6 or NONE If the address in not IPv4 or IPv6.
Constraints
Example
Input
123.123.000.254
Output
IPv4
"""
import re

address = input()

# Check if the address is IPv4
ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
if re.match(ipv4_pattern, address):
    parts = address.split('.')
    if all(0 <= int(part) <= 255 for part in parts):
        print("IPv4")
        exit()

# Check if the address is IPv6
ipv6_pattern = r'^([0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}$'
if re.match(ipv6_pattern, address):
    print("IPv6")
    exit()

# If the address is neither IPv4 nor IPv6
print("NONE")
