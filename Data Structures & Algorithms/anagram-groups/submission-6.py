class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_map = defaultdict(list)
        for word in strs:
            idx_list = [0]*26
            for ch in word:
                idx_list[ord(ch)-97] += 1

            char_map[tuple(idx_list)].append(word)

        return list(char_map.values())