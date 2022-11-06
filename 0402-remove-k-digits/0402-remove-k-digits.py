class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # [1,2,3,4,5]
        # [5,4,3,2,1]
        stack = []
        for c in num:
            while k > 0 and stack and stack[-1] > c:
                k -= 1
                stack.pop()
            stack.append(c)
        stack = stack[:len(stack) - k]
        res = "".join(stack)
        return str(int(res)) if stack else "0"