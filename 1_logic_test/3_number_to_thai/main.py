"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""

class Solution:
    default_number_convert = ["ศูนย์", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
    default_position_convert = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]
    default_max_number = 10_000_000

    def __init__(
        self,
        number_convert: list | None = None,
        position_convert: list | None = None,
        max_number: int | None = None
    ):
        self.number_convert = list(number_convert) if number_convert is not None else list(self.default_number_convert)
        self.position_convert = list(position_convert) if position_convert is not None else list(self.default_position_convert)
        self.max_number = int(max_number) if max_number is not None else int(self.default_max_number)

    def number_to_thai(self, number: int) -> str:
        # validate
        if not isinstance(number, int) or isinstance(number, bool):
            return "invalid input"
        if number < 0:
            return "number can not less than 0"
        if self.max_number is not None and number > self.max_number:
            return f"number can not more than {self.max_number}"
        if number == 0:
            return self.number_convert[0]

        num_str = str(number)
        length = len(num_str)
        thai = ""

        cycle_len = len(self.position_convert) - 1
        has_prev_digit_in_group = False

        for index, char in enumerate(num_str):
            digit = length - index - 1
            digit_mod = digit % cycle_len
            
            pos_str = self.position_convert[digit_mod]
            num_str = self.number_convert[int(char)]

            # specific condition 
            if char == "0":
                num_str = ""
                pos_str = ""
            else:
                if digit_mod == 1 and char == "1":
                    num_str = ""
                if digit_mod == 1 and char == "2":
                    num_str = "ยี่"
                if digit_mod == 0 and length > 1 and char == "1" and has_prev_digit_in_group:
                    num_str = "เอ็ด"
                has_prev_digit_in_group  = True
                
            if digit_mod == len(self.position_convert)-1 and digit > 1 and char == "0":
                pos_str = pos_str+"ล้าน"

            thai = thai+f"{num_str}{pos_str}"
            if digit_mod == 0:
                if digit > 0:
                    thai += self.position_convert[len(self.position_convert)-1]
                has_prev_digit_in_group = False

            last_number = char

        return thai