class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        seen = defaultdict(int)
        mx = 0
        left, right = 0, 0

        for right in range(len(s)):
            seen[s[right]] += 1
            mx = max(mx, seen[s[right]])
            cond = ((right - left + 1) - mx) <= k
            
            if not cond:
                seen[s[left]] -= 1
                left += 1
            
            ans = max(ans, right-left+1)

        return ans
            





