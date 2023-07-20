from collections import Counter
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        char_array = [0] * 26
        offset = ord('a')

        original_letters = Counter(words[0])
        for char, count in original_letters.items():
            char_array[ord(char) - offset] = count

        for i in range(1, len(words)):
            letters = Counter(words[i])

            # Update char_array based on the characters present in each word
            for char in list(original_letters.keys()):
                char_array[ord(char) - offset] = min(char_array[ord(char) - offset], letters.get(char, 0))

        # Use list comprehension to construct the result directly
        common_chars = [chr(offset + idx) for idx, count in enumerate(char_array) for _ in range(count)]

        return common_chars
