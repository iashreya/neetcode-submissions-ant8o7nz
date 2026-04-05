class Solution:
    def isAlphNum(self, ch):
        order = ord(ch)
        if ((order > 47 and order < 58) or
            (order > 64 and order < 91) or
            (order > 96 and order < 122)):
            return True
        else:
            return False

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while(left < right):
            if not(self.isAlphNum(s[left]) or self.isAlphNum(s[right])):
                left += 1
                right -= 1
            elif not self.isAlphNum(s[left]):
                left += 1
            elif not self.isAlphNum(s[right]):
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        
        return True