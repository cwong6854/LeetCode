class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        index = len(digits) - 1
        count = 0
        total = 0 
        while length > 0:
            if index == 0:
                total += digits[index] * 10 ** count + 1
                length -= 1
                index -= 1
                count += 1
            else:
                total += digits[index] * 10 ** count
                length -= 1
                index -= 1
                count += 1
        lst = []
        while total != 0:
            lst.insert(0, total % 10)
            total = total // 10
        return lst
            