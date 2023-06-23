"""
Current config for the mad pod racing challenge 
Current Silver League 
"""


import sys
import math
while True:
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]
    if next_checkpoint_angle > 90 or next_checkpoint_angle < -90:
        print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " 15")
    elif next_checkpoint_angle == 0: 
        print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " BOOST")
    else:
        print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " 100")
 
