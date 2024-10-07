'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M. Symbol
Value
I 1
V 5
X 10
L 50
C 100
D 500
M 1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply
X + II.The number27 is written as XXVII, which is XX + V + II.

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V = 5, III = 3.
Example
3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i, c in enumerate(s):
            if (i + 1) == len(s) or roman_numerals[c] >= roman_numerals[s[i + 1]]:
                result += roman_numerals[c]
            else:
                result -= roman_numerals[c]
        return result

roman = input("Введите римскую цифру: ")
print(Solution().romanToInt(roman))
