class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        lst = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                lst += ["FizzBuzz"]
            elif i % 5 == 0:
                lst += ["Buzz"]
            elif i % 3 == 0:
                lst += ["Fizz"]
            else:
                lst += [str(i)]
        return lst