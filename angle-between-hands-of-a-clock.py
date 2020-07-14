# Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

# Constraints:

# 1 <= hour <= 12
# 0 <= minutes <= 59
# Answers within 10^-5 of the actual value will be accepted as correct.

class Solution(object):
    def angleClock(self, hour, minutes):
        degrees = abs((minutes * 6) - ((minutes * 0.5) + 30 * (0 if hour == 12 else hour)))

        return degrees if degrees <= 180 else 360 - degrees