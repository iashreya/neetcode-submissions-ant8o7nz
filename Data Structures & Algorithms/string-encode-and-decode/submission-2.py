import hashlib
from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        all_words = "".join(strs)
        delimiter = ""
        
        while(True):
            hash_value = hashlib.sha256().hexdigest()
            if hash_value not in all_words:
                delimiter = hash_value
                break
        
        encoded_string = ""
        for str in strs:
            encoded_string += delimiter
            encoded_string += str

        return encoded_string
            


    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        hash_value = s[:64]
        s = s[64:]
        return s.split(hash_value)