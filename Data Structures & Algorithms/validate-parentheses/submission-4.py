class Solution:
    def isValid(self, s: str) -> bool:
        closing = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        openBrackets = []
        for c in s:
            if c in closing.keys():
                openBrackets.append(c)
            elif len(openBrackets) == 0:
                openBrackets.append(c)
                break
            elif closing[openBrackets[-1]] != c:
                break
            else:
                openBrackets.pop()
        return len(openBrackets)==0