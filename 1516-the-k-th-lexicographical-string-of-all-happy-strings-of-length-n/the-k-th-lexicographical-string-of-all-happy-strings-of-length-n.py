class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        valid_chars = 'abc'
        total_happy_strings = 3 * pow(2, n-1)
        if k > total_happy_strings:
            return ''
        res,left,right = '', 1, total_happy_strings
        for i in range(n):
            partition_size = (right - left + 1) / len(valid_chars)
            selected_char_index = int((k - 1) // partition_size)
            selected_char = valid_chars[selected_char_index]
            res+=selected_char
            valid_chars= 'abc'.replace(selected_char, '')
            k = int(k % partition_size) if k > partition_size else k
            left = (selected_char_index * partition_size) + 1
            right = (selected_char_index + 1) * partition_size

        return res


        