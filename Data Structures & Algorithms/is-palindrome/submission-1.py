class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        valid_chr = [chr(i) for i in range(48,58)] + [chr(i) for i in range(97,123)]
        st = ""
        for i in s:
            if i in valid_chr:
                st += i

        mid = len(st)//2
        
        for i in range(mid):
            if st[i] != st[-1-i]:
                return False

        return True