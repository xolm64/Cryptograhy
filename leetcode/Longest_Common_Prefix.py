'''Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix,
return an empty string "".
Example
1:
Input: strs = ["flower", "flow", "flight"]
Output: "fl"
Example
2:
Input: strs = ["dog", "racecar", "car"]
Output: ""
Explanation: There is no common prefix among the input strings.'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """


        prefix = ''
        for i in range(min(map(len, strs))):
            if all(s[i] == strs[0][i] for s in strs):
                prefix += strs[0][i]
            else:
                break

        return prefix