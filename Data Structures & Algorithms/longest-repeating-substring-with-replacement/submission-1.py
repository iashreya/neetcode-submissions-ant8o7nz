class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        1. Initialize left and right pointers
        2. Keep a hash_map of count of chars
        3. Loop over the string
        4. Keep a chr_count hash map
        5. If window is valid
            5.a. update ans
        5. If invalid
            5.a. reduce char count of removed element from map
            5.b. increment left by 1
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

