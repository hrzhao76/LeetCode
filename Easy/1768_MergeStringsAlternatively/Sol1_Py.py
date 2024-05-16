class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ret_str = ""
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            ret_str += word1[i]
            ret_str += word2[i]

        remaining_str = word1[min_len:] if len(word1) > len(word2) else word2[min_len:]
        return ret_str + remaining_str