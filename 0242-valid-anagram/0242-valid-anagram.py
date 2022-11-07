class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        anagram = {}
        ana = True
        if len(s) != len(t):
            return False
        for c in s:
            if c not in anagram:
                anagram[c] = 1
            else:
                anagram[c] += 1
        
        for c in t:
            if c in anagram:
                anagram[c] -= 1
            
        for i in anagram:
            if anagram[i] > 0:
                ana = False
        return ana