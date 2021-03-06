# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.



# Example:

# Input:
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]

# Output: 16

# Explanation: The perimeter is the 16 yellow stripes in the image below:

# 1) nested loop and dynamic programming
# O(MN) time complexity, O(1) space
# for example a cell has its upper, lower, left and right to be land as well. The perimeter added will be zero, offset by 4
class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        perimeter = 0

        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1):
                    offset = (1 if (i-1>=0 and grid[i-1][j]==1) else 0)+ (1 if (j-1>=0 and grid[i][j-1]==1) else 0) + (1 if (i+1<m and grid[i+1][j]==1) else 0) + (1 if (j+1<n and grid[i][j+1]==1) else 0)
                    perimeter += 4 - offset
                    #print((i,j),offset,perimeter)
        return perimeter

# 2)  ne(a, b) is equivalent to a != b
# count the differing pairs, both horizontally and vertically
# list(map(list, zip(*grid))) is transposing the matrix
import operator
class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return sum([operator.ne([0]+row, row+[0]) for row in grid + list(zip(*grid))])

# 3) variant of 1)
# O(MN) time
class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0]) if grid else 0
        return sum([(r - 1 < 0  or grid[r-1][c] == 0) +
                    (c - 1 < 0  or grid[r][c-1] == 0) +
                    (r + 1 >= m or grid[r+1][c] == 0) +
                    (c + 1 >= n or grid[r][c+1] == 0)
                    for r in range(m)
                    for c in range(n)
                    if grid[r][c] == 1]
                    )

# 4)
class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        s, m = len(grid), len(grid[0])
        ans = 0
        for x in range(s):
            for y in range(m):
                if grid[x][y] == 1:
                    ans += 4
                    if x < s - 1 and grid[x+1][y] == 1:
                        ans -= 2
                    if y < m - 1 and grid[x][y+1] == 1:
                        ans -= 2
        return ans
