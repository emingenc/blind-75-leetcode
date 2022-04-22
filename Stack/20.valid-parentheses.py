class Solution:
    def isValid(self, s: str) -> bool:
        parantheses = { '(': ')', '{': '}', '[': ']' }
        stack = []
        for char in s:
            if parantheses.get(char):
                stack.append(char)
            elif not stack or parantheses[stack.pop()] != char:
                return False
        return True if not stack else False

""" Here is the explanation for the code above:
1. We first create a dictionary called parantheses.
2. We then create an empty stack called stack.
3. We then iterate through the string s.
4. If char is in the parantheses dictionary, we append it to the stack.
5. Else, if stack is empty or the parantheses[stack.pop()] is not equal to char, we return False.
6. When the loop is finished, if stack is empty, we return True, otherwise we return False. """
