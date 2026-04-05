class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Steps:
        1. Keep a map of alphabets that have been seen and at what index
        2. Initialize ans = 0
        3. Loop over the string with idx i
            3.a. ans = max(ans, i-map.get(s[i]))
            3.b. map[s[i]] = i
        """
        last_seen = {}
        ans = 0
        l, r = 0, 0

        for r in range(len(s)):
            if s[r] in last_seen:
                l = max(last_seen[s[r]]+1, l)
            
            last_seen[s[r]] = r
            ans = max(ans, r-l+1)
                

        return ans

