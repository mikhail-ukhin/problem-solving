# There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.

# The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.

# If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

# You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks. 

# Input: [[1,2,2,1], - [1, 1, 1, 1, 1, 1]
#         [3,1,2],
#         [1,3,2],
#         [2,4],
#         [3,1,2],
#         [1,3,1,1]]

class Solution:
    def leastBricks(self, wall) -> int:
        row_len = sum(wall[0])
        matches = [0] * row_len
        max_gap = 0

        for row in wall:
            row_sum = 0

            for brick in row:
                row_sum += brick

                if (row_sum < row_len):
                    matches[row_sum] += 1
                    max_gap = max(matches[row_sum], max_gap)

        return len(wall) - max_gap
