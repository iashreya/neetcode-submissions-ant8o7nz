class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for str in strs:
            count = [0]*26
            for c in str:
                count[ord(c)-ord('a')] += 1
            if res.get(tuple(count)):
                res[tuple(count)].append(str)
            else:
                res[tuple(count)] = [str]

        return list(res.values())

        