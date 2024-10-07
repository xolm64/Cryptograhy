'''Given a string s, find the length of the longest substring without repeating characters.
Example
1:
Input: s = "abcabcbb"
Output: 3
Explanation: The
answer is "abc",
with the length of 3.
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.s = s
        if self.s =='':
            k = 0
        else:
            new_str = ''
            for elem in self.s:
                  for i in self.s:
                    if elem != i:
                        new_str = elem + i
            k = len(new_str)
        return k

s = "abcabcbb"

print(Solution().lengthOfLongestSubstring(s))