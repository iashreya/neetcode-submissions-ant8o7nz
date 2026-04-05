class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        1. Initialize left and right pointers
        2. Loop over the string
        3. Move right pointer by one as long as the window is valid
        4. Keep a hash_map of count of chars
        5. Move left pointer when window becomes invalid; update ans = max(ans, window_length)
        6. Window is valid if window_length - max(hash_map) <= k
        """

        left, right = 0, 0
        ans = 0
        chr_count = defaultdict(int)

        for right in range(len(s)):
            window_len = right - left + 1
            chr_count[s[right]] += 1
            if window_len - max(chr_count.values()) <= k:
                ans = max(ans, window_len)
            else:
                chr_count[s[left]] -= 1
                left += 1

        return ans

