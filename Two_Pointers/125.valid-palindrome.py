class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1

        return True

""" Here is the explanation for the code above:
1. We use a while loop to go through the string.
2. We compare the current left index with the right index, if they are not alphanumeric,
   we increment/decrement the index accordingly.
3. We do the same thing for the right index as well.
4. We compare the lower case of the left and right index, if they are not equal,
   we return False.
5. Finally, we return True. """
