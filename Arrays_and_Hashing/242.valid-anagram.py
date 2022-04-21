class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        for c in s:
            if chars.get(c) is None:
                chars[c] = 1
            else:
                chars[c] += 1
        for c in t:
            if chars.get(c) is None:
                return False
            else:
                chars[c] -= 1
        for v in chars.values():
            if v != 0:
                return False
        return True
      
""" Here is the explanation for the code above:
1. We use a dictionary to store the characters and their counts.
2. We loop through the first string and count the number of times each character appears.
3. We loop through the second string and decrement the count for each character.
4. When we have looped through both strings, we loop through the values in the dictionary.
    If a value is non-zero, we return False. """
