class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for i in range(len(s)):
            if s[i] == "I":
                if len(s) == 1 or i == len(s) - 1:
                    total += 1
                else:
                    if s[i + 1] == "V":
                        total -= 1
                    elif s[i + 1] == "X":
                        total -= 1
                    else:
                        total += 1
            if s[i] == "V":
                total += 5
            if s[i] == "X":
                if len(s) == 1 or i == len(s) - 1:
                    total += 10
                else:
                    if s[i + 1] == "L":
                        total -= 10
                    elif s[i + 1] == "C":
                        total -= 10
                    else:
                        total += 10
            if s[i] == "L":
                total += 50
            if s[i] == "C":
                total += 100
            if s[i] == "D":
                if len(s) == 1 or i == 0:
                    total += 500
                else:
                    if s[i - 1] == "C":
                        total += 300
                    else:
                        total += 500
            if s[i] == "M":
                if len(s) == 1 or i == 0:
                    total += 1000
                else:
                    if s[i - 1] == "C":
                        total += 800
                    else:
                        total += 1000
        return total