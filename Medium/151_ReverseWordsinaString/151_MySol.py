class Solution:
    def reverseWords(self, s: str) -> str:
        # words = s.strip().split(' ') # 
        # words = [word for word in words if word != '']
        words = s.split() # will remove any whitespace
        return " ".join(words[::-1])
    
s = "a good   example"
worker = Solution()
worker.reverseWords(s)