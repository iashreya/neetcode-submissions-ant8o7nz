class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        ans = 0

        stack = {}
        while(right < len(s)):
            if s[right] not in stack:
                stack[s[right]] = right
            else:
                left = max(left, stack[s[right]] + 1)
                stack[s[right]] = right
            
            ans = max(ans, right-left+1)
            right += 1

        return ans

                