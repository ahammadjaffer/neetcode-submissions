class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = sorted(list(s))
        list2 = sorted(list(t))
        if list1 != list2:
            return False
        return True
        