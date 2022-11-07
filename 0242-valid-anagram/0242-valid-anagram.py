class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        # hashmap -> letter with counts
        anagram = {}
        for c in s:
            if c not in anagram:
                anagram[c] = 1
            else:
                anagram[c] += 1
        for c in t:
            if c in anagram:
                anagram[c] -= 1
                if anagram[c] == 0:
                    anagram.pop(c)
        return True if len(anagram) == 0 else False
        