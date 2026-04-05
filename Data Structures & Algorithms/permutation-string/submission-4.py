class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        left = 0
        s1_map = [0]*26
        for i in s1:
            s1_map[ord(i)-97] += 1
        win_map = [0]*26
        for i in range(len(s1)):
            win_map[ord(s2[i])-97] += 1

        if win_map == s1_map:
            return True 
        win_map[ord(s2[left])-97] -= 1
        left += 1
        for right in range(len(s1), len(s2)):
            win_map[ord(s2[right])-97] += 1
            if win_map == s1_map:
                return True
            else:
                win_map[ord(s2[left])-97] -= 1
                left += 1

        return False
