import sys
import math

# Read the number of temperatures to analyze
n = int(input())

# Read the temperatures as a string
temperatures = input().split()

# Initialize the closest temperature to a large positive value
closest_temperature = sys.maxsize

# Iterate through each temperature
for temperature in temperatures:
    # Convert the temperature to an integer
    temperature = int(temperature)

    # Check if the absolute value of the current temperature is closer to zero than the closest temperature so far
    if abs(temperature) < abs(closest_temperature) or (abs(temperature) == abs(closest_temperature) and temperature > closest_temperature):
        closest_temperature = temperature

# Print the closest temperature to zero
print(closest_temperature if n > 0 else 0)