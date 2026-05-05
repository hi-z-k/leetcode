class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        cleaned = []
        is_comment = False
        cleaned_line = []
        
        for line in source:
            i = 0
            while i < len(line):
                if is_comment:
                    if i + 1 < len(line) and line[i:i+2] == "*/":
                        is_comment = False
                        i += 1
                else:
                    if i + 1 < len(line) and line[i:i+2] == "/*":
                        is_comment = True
                        i += 1
                    elif i + 1 < len(line) and line[i:i+2] == "//":
                        break
                    else:
                        cleaned_line.append(line[i])
                i += 1
            
            if not is_comment and cleaned_line:
                cleaned.append("".join(cleaned_line))
                cleaned_line = []
                
        return cleaned