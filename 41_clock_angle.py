"""
Problem 41: Clock Angle
Statement: Clock Angle: Given hour and minute, calculate the smaller angle between the two hands
"""

hour = int(input("Enter hour (0-12): "))
minute = int(input("Enter minute (0-59): "))

# Angle of hour hand and minute hand from 12 o'clock position
hour_angle = (hour % 12) * 30 + minute * 0.5
minute_angle = minute * 6

angle = abs(hour_angle - minute_angle)

# The smaller angle between the two hands
if angle > 180:
    angle = 360 - angle

print("The angle between the clock hands is:", angle, "degrees")
