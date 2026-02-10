class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        data = defaultdict(list)
        for directory in paths:
            path, *files = directory.split(" ")
            for f in files:
                filename, content = f.split("(")
                data[content].append(f"{path}/{filename}")
        duplicates = [fileList for fileList in list(data.values()) if len(fileList) > 1]
        
        return duplicates