class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            # check if char in s and char in t are equal
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        # if all chars in s are traversed, it means that we found it
        if i == len(s):
            return True
        # however, if all chars in t are traversed but, still s isnt being traversed full, then we didnt find the subsequence
        if j ==len(t) and i < len(s):
            return False
