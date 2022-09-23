class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # find longest string w/o repeating characters
        
        lst = []
        list_dic = []
        
        # if not in dic, put letter into dic
        # check length of dic at end of loop
        largestLength = 0
        
        for i in range(len(s)):
            if s[i] not in lst:
                lst.append(s[i])
            else:
                if s[i - 1] == s[i]:
                    list_dic.append(len(lst))
                    lst = []
                    lst.append(s[i])
                if lst.index(s[i]) != i:
                    list_dic.append(len(lst))
                    lst = lst[lst.index(s[i]) + 1:]                    
                    lst.append(s[i])              
        list_dic.append(len(lst))
        largestLength = max(list_dic)
        return largestLength
#         "anviaj"
#         "ckilbkd"
        
                