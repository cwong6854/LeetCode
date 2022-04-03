class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        length = len(str(x))
        if length == 0:
            return False
        else:
            x_str = str(x)
            lst = []
            for i in range(len(x_str)):
                lst.append(x_str[i])
            print(lst)
            if lst == list(reversed(lst)):
                return True
            else:
                return False
            # if length % 2 == 0:
            #     for i in range(int(length / 2), ):
                    
        