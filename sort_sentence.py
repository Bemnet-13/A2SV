class Solution:
    def sortSentence(self, s):
        words = s.split()
        words.sort(key = lambda word : word[-1])

        corr_sentence = ""
        for i in range(len(words)):
            words[i] = words[i][:len(words[i])-1]
        
        return " ".join(words)
