class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = [folder for folder in path.split("/") if folder]
        stack = []
        print(directories)
        for folder in directories:
            if folder == "..":
                if stack:
                    stack.pop()
            elif folder == ".":
                continue
            else:
                stack.append(folder)
        return "/"+"/".join(stack)