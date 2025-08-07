Approach 1
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False 

        s_counts={}
        t_counts={}

        for char in s:
           s_counts[char]=s_counts.get(char,0)+1

        for char in t:
           t_counts[char]=t_counts.get(char,0)+1

        return s_counts == t_counts

Approach 2
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        

        if sorted(s) == sorted(t):
            return True
        else:
            return False
