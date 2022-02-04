class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        for i in range(numRows - 1):
            x = [0] + res[-1] + [0]
            row = []
            for j in range(len(x) - 1):
                row.append(x[j] + x[j + 1])
            res.append(row)
        return res