class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s, len_t = len(s), len(t)
        pointer_s, pointer_t = 0, 0
        while pointer_s < len_s and pointer_t < len_t:
            if s[pointer_s] == t[pointer_t]:
                pointer_s += 1 
            pointer_t += 1

        if pointer_s == len_s:
            return True
        return False 