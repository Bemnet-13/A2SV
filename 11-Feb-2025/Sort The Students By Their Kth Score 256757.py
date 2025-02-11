# Problem: Sort The Students By Their Kth Score - https://leetcode.com/problems/sort-the-students-by-their-kth-score/

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        # Bubble sort over the array to avoid space consumption

        for i in range(len(score)):
            for j in range(i + 1, len(score)):
                if score[i][k] < score[j][k]:
                    for p in range(len(score[0])):
                        score[i][p], score[j][p] = score[j][p], score[i][p]
        
        return score