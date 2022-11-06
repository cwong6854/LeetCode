class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # algorithm -> monotonic increasing stack
        stack = []
        # go through each number
        for c in num:
            # k operations
            while k > 0 and stack and stack[-1] > c: # while k isn't 0 and stack is non-empty
                print(stack[-1])
                k -= 1
                stack.pop()
            stack.append(c)
        stack = stack[:len(stack) - k]
        print(stack)
        x = "".join(stack)
        return str(int(x)) if x else "0"
        
        