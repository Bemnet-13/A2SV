class Solution:
    def sortPeople(self, names, heights):
        name_height = []
        for i in range(len(names)):
            person = [names[i], heights[i]]
            name_height.append(person)
        name_height.sort(key = lambda n : n[1], reverse = True)
        name_sorted = [p[0] for p in name_height]
        return name_sorted
