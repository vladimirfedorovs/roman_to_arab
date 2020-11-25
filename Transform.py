class Solution:
    def romanToInt(self,s: str) -> int:
        res = 0
        roman_to_arab = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        if 0<len(s)<16:

            for i in range(len(s) - 1):
                if (roman_to_arab[s[i]] < roman_to_arab[s[i + 1]]):
                    res -= roman_to_arab[s[i]]
                elif (roman_to_arab[s[i]] >= roman_to_arab[s[i + 1]]):
                    res += roman_to_arab[s[i]]

            res += roman_to_arab[s[len(s) - 1]]

        else:
            res = 'Введите число с количеством знаков от 1 до 15'
        return res




s = input('Введите римское число n = ')
print(Solution().romanToInt(s))

