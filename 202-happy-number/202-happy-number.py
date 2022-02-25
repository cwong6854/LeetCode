class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        total = 0
        n_str = str(n)
        count = 10
        while total != 1 or count != 0:
            for i in n_str:
                total += int(i)**2
            print(total)
            n_str = str(total)
            if total == 1:
                return True
            elif count == 0:
                return False
            else:
                total = 0
                count -= 1