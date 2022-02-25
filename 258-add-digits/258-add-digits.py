class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = str(num)
        total = 0
        if num < 10:
            return num
        else:
            while len(num_str) > 1:
                for i in num_str:
                    total += int(i)
                    print(num_str)
                if total >= 10:
                    num_str = str(total)
                    total = 0
                else:
                    return total