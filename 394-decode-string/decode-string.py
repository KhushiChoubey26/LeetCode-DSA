class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                # Get the encoded string
                encoded = ''
                while stack[-1] != '[':
                    encoded = stack.pop() + encoded
                stack.pop()  # remove the '['

                # Get the repeat count
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                k = int(k)

                # Repeat and push back
                stack.append(encoded * k)

        return ''.join(stack)
