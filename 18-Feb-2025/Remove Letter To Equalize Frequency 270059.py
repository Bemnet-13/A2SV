# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = Counter(word)
        counts = Counter(counter.values())

        if len(counts) > 2:
            return False
        elif len(counts) == 1 and 1 in counts or len(counter) == 1:
            return True
        elif len(counts) == 1:
            return False
        elif len(counts) == 2:
            min_, max_ = min(counts.keys()), max(counts.keys())

            if counts[min_] == 1 and min_ == 1:
                return True
            # elif 
            elif counts[max_] != counts[min_] and counts[max_] > 1:
                return False
            elif counts[max_] == 1 and max_ - min_ == 1:
                return True
            else:
                return False


        

        # if len(counts) != 2 and len(counter) == 1 or 1 in counts:
        #     return True
        # elif len(counts) != 2 and len(counter) >= 2:
        #     return False
        # elif len(counts) == 2:
