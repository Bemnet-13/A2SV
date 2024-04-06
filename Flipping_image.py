class Solution:
    def flipAndInvertImage(self, image):
        for lst in image:
            lst.reverse()
            for i in range(len(lst)):
                if lst[i] == 0:
                    lst[i] = 1
                else:
                    lst[i] = 0
        
        return image
        
trial =Solution()
o = trial.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])
print(o)