# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        on_block = False
        curr_line = []
        last_block = (-1, -1)
        for line_num, line in enumerate(source):
            i = 0
            while i < len(line):
                # If on a block comment, do not consider line comments
                if on_block and i - 1 < len(line) and i + 1 < len(line) and line[i - 1:i + 2] == "/*/":
                    if (line_num, i - 1) != last_block:
                        on_block = False
                    i += 1
                # End the block comment here
                elif on_block and i + 1 < len(line) and line[i] + line[i + 1] == "*/":
                    on_block = False
                    i += 1
                elif not on_block and i + 1 < len(line) and line[i] + line[i + 1] == "//":
                    break
                elif not on_block and i + 1 < len(line) and line[i] + line[i + 1] == "/*":
                    on_block = True
                    last_block = (line_num, i)
                elif not on_block:
                    # print("here", line[i])
                    curr_line.append(line[i])

                i += 1
            

            if not on_block and curr_line != []:
                ans.append("".join(curr_line))
                curr_line = []
        return ans
            
