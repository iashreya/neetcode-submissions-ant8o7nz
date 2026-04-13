class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_map = {}
        for word in strs:
            idx_list = [0]*26
            for ch in word:
                idx_list[ord(ch)-97] += 1
            
            if tuple(idx_list) in char_map:
                char_map[tuple(idx_list)].append(word)
            else:
                char_map[tuple(idx_list)] = [word]

        return list(char_map.values())