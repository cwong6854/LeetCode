class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # count = 0
        # count_s = 0
        # count_t = 0
        # unique = set(t)
        # total_letters = len(unique)
        # while count < total_letters:
        #     for i in unique:
        #         if i in s:
        #             for j in range(len(s)):
        #                 if s[j] == i:
        #                     count_s += 1
        #             for k in range(len(t)):
        #                 if t[k] == i:
        #                     count_t += 1
        #             if count_s == count_t:
        #                 count_s = 0
        #                 count_t = 0
        #                 continue
        #             else:
        #                 return i
        #         else:
        #             return i
        unique = set(t)
        for i in unique:
            if s.count(i) < t.count(i):
                return i
        return None
                    
            