from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        l, r = 0, 0
        seen = Counter(t)
        match = []
        ans = "*" * 1000
        
        while r < len(s):
            if s[r] not in seen:
                if l == r:
                    l += 1
            else:
                match.append(r)
                seen[s[r]] -= 1

                while sum(max(0, v) for v in seen.values()) == 0:
                    # update answer
                    if (r - l + 1) <= len(ans):
                        ans = s[l:r+1]

                    # Shrink Window step-by-step
                    if s[l] in seen:
                        seen[s[l]] += 1
                        if match and match[0] == l:
                            match.pop(0)

                    l += 1 

            r += 1

        return ans if ans != "*" * 1000 else ""
