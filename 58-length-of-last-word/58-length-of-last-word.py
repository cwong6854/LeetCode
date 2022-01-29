class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        return len(words[len(words) - 1])
        # word = ""
        # if len(s.split()) == 1:
        #     word = s.split()
        #     return len(word[0])
        # else:
        #     for i in range(len(s) - 1, -1, -1):
        #         if s[i] != " ":
        #             word += s[i]
        #         elif len(word) == 0:
        #             continue
        #         else:
        #             return len(word)