class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        lst = []
        transpose = []
        index = 0
        count = len(matrix[0])
        while count != 0:
            for i in range(len(matrix)):
                transpose.append(matrix[i][index])
            lst.append(transpose)
            transpose = []
            index += 1
            count -= 1
        return lst