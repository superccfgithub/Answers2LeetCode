#question name:Power of two
#question link:https://leetcode.com/problems/power-of-two/
#Runtime: 52 ms

#-------------------Submitted Code-------------------------
class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        if not n & (n-1):
            return True
        return False