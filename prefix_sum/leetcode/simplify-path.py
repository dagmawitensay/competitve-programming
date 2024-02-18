class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")

        for directory in path:
            if directory == "..":
                if stack:
                    stack.pop()
                else:
                    continue
            elif directory != "" and directory != ".":
                stack.append(directory)
        
        return "/" + "/".join(stack)