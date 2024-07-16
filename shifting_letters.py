class Solution:
    def shiftingLetters(self, s: str, shifts) -> str:
        shifted_s = ""

        for i in range(len(s)):
            letter = s[i]
            shift = 0
            for sh in shifts:
                if i in range(sh[0], sh[1] + 1):
                    if sh[2] == 0:
                        shift -= 1
                    else:
                        shift += 1
            
            l = chr((((ord(letter) - 97) + shift) % 26) + 97)
            shifted_s += l
        return shifted_s

trial = Solution()
o = trial.shiftingLetters(s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]])
print(o)