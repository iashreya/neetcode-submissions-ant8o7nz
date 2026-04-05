class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        valid_chr = [chr(i) for i in range(48,58)] + [chr(i) for i in range(97,123)]
        st = ""
        for i in s:
            if i in valid_chr:
                st += i

        mid = len(st)//2
        i, j = 0, len(st)-1
        while(i<j):
            if st[i]!=st[j]:
                return False
            i += 1
            j -= 1
            
        return True