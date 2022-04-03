class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """        
        x = str(x)
        if list(x) == list(reversed(x)):
            return True
        