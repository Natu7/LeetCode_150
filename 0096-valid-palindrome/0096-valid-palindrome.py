class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = []
        st = s.lower()
        for i in st:
            if i.isalnum():
                l.append(i)
        if l == l[::-1]:
            return True