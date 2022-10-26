class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # store the frequencies of each letter in hash
        # why have frequenicies of each letter?
        # --> replacement cost -> dist between left & right - highest freq
        # if <= k, then move forward and increase freq of letter by 1
        # if > k, then reduce left pointer freq by 1
        # if not in freq: pop the left pointer freq and increase left pointer by 1
        # keep track of left and right index
        # also keep track of the longestSubstring 
        freq = {}
        longestSubstring = 0
        l = 0
        
        for r in range(len(s)):
            if s[r] not in freq:
                freq[s[r]] = 0
            freq[s[r]] += 1
            
            # Replacement cost
            dist_lr = r - l + 1
            if dist_lr - max(freq.values()) <= k:
                longestSubstring = max(dist_lr, freq[s[r]])
            
            else:
                freq[s[l]] -= 1
                if s[l] not in freq:
                    freq.pop(s[l])
                l += 1
            
        return longestSubstring
                
            