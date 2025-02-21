# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pairs = list(zip(names, heights))
        pairs.sort(key = lambda pair : pair[1], reverse = True)

        return [pair[0] for pair in pairs]