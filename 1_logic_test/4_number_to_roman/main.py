"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:
    block_one   = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    block_two   = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    block_three = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    block_four  = ["M", "MM", "MMM", "(IV)", "(V)", "(VI)", "(VII)", "(VIII)", "(IX)"]
    max_number  = 100_000_000

    def _mutual_thousand(self, num: str) -> str:
        return f"({num})"

    def _mutual_hundret_thousand(self, num: str) -> str:
        return f"|{num}|"

    def _convert_under_thousand(self, n: int) -> str:
        res = ""
        if n >= 100:
            res += self.block_three[(n // 100) - 1]
            n %= 100
        if n >= 10:
            res += self.block_two[(n // 10) - 1]
            n %= 10
        if n >= 1:
            res += self.block_one[n - 1]
        return res

    def number_to_roman(self, number: int) -> str:
        # validate
        if not isinstance(number, int) or isinstance(number, bool):
            return "invalid input"
        if number < 0:
            return "number can not less than 0"
        if number == 0:
            return ""
        if number >= self.max_number:
            return "number can not over then 99,999,999"

        roman_text = ""

        if number >= 100_000:
            hundred_thousands = number // 100_000
            converted_ht = self._convert_under_thousand(hundred_thousands)
            roman_text += self._mutual_hundret_thousand(converted_ht)
            number %= 100_000

        if number >= 10_000:
            ten_thousands = number // 10_000
            roman_text += self._mutual_thousand(self.block_two[ten_thousands - 1])
            number %= 10_000

        if number >= 1_000:
            thousands = number // 1_000
            roman_text += self.block_four[thousands - 1]
            number %= 1_000

        roman_text += self._convert_under_thousand(number)

        return roman_text