class Solution:
    def intToRoman(self, num):
        roman = ""
        storeInt = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        storeRoman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        for i in range(len(storeInt)):
            while num >= storeInt[i]:
                roman += storeRoman[i]
                num -= storeInt[i]
        return roman

solution = Solution()
print(solution.intToRoman(3))     # Output: 'III'
print(solution.intToRoman(58))    # Output: 'LVIII'
print(solution.intToRoman(1994))  # Output: 'MCMXCIV'
