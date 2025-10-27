class Solution:
    def simplifyPath(self, path: str) -> str:
        directoryList = [dir for dir in path.split("/") if dir != ""]
        stack = []
        for dir in directoryList:
            if dir == "..":
                try:
                    stack.pop()
                except IndexError:
                    pass
                continue
            elif dir == ".":
                continue
            stack.append(dir)
        path = "/" + "/".join(stack)
        return path