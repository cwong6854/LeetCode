class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # scan with two pointers: left and right
        # store frequencies of each letter
        # replacement cost: dist between left and right - highest frequency
        
        # edge cases:
        # no letters
        # 1 letter
        # all same letter
        # unique letters
        
        left = 0
        longestSubstring = 0
        dic = {}
        for r in range(len(s)):
            if s[r] not in dic:
                dic[s[r]] = 0
            dic[s[r]] += 1
            
            # Replacement cost
            replacement = r - left + 1
            if replacement - max(dic.values()) <= k:
                longestSubstring = max(longestSubstring, replacement)
            else:
                dic[s[left]] -= 1
                if not dic[s[left]]:
                    dic.pop(s[left])
                left += 1                
        return longestSubstring
                                    
		
        
                    
                
            