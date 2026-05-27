class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return ""
        
        stack = []
        stringBuilder = ""
        
        for c in path:
            if c == "/":
                if stringBuilder:
                    if stringBuilder == ".":
                        pass
                    elif stringBuilder == "..":
                        if stack:
                            stack.pop()
                    else:
                        stack.append(stringBuilder)
                    stringBuilder = ""
            else:
                stringBuilder += c

        if stringBuilder:
            if stringBuilder == "..":
                if stack:
                    stack.pop()
            elif stringBuilder != ".":
                stack.append(stringBuilder)

        res = ''
        for i, d in enumerate(stack):
            res += d
            if i != len(stack) - 1:
                res += '/'
        
        return '/' + res