class Solution:
    def find_sign(self, s):
        sign = ""
        char_map = {chr(i): 0 for i in range (97,123)}
        for ch in s:
            char_map[ch] += 1    
        sign = "".join([i*char_map[i] for i in char_map])
        return sign

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sign_words_map = {}

        for str in strs:
            str_sign = self.find_sign(str)
            if sign_words_map.get(str_sign):
                sign_words_map[str_sign].append(str)
            else:
                sign_words_map[str_sign] = [str]

        return list(sign_words_map.values())

        