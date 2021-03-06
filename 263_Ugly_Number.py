# Write a program to check whether a given number is an ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

# Example 1:

# Input: 6
# Output: true
# Explanation: 6 = 2 × 3
# Example 2:

# Input: 8
# Output: true
# Explanation: 8 = 2 × 2 × 2
# Example 3:

# Input: 14
# Output: false
# Explanation: 14 is not ugly since it includes another prime factor 7.
# Note:

# 1 is typically treated as an ugly number.
# Input is within the 32-bit signed integer range: [−231,  231 − 1].

# https://leetcode.com/problems/ugly-number/description/

# 1) recursive approach
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2: return num == 1

        elif num % 5 == 0:
            return self.isUgly(num/5)
        elif num % 3 == 0:
            return self.isUgly(num/3)
        elif num % 2 == 0:
            return self.isUgly(num/2)
        else:
            return False

# 2) iterative approach
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for p in 2, 3, 5:
            # one line condition for num % p==0 and num > 0
            while num % p == 0 < num:
                num /= p
        return num == 1

# 3) mathematics operations
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 == 30**32 % num
