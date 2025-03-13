# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def play_game(i, j, nums, turn):
            k = turn % 2
            if i == j:
                return nums[i] if k == 1 else -nums[i]

            
            if k == 0:
                ans1 = -nums[i] + play_game(i + 1, j, nums, turn + 1)
                ans2 = -nums[j] + play_game(i, j - 1, nums, turn + 1)
                return min(ans1, ans2)
            else:
                ans1 = nums[i] + play_game(i + 1, j, nums, turn + 1)
                ans2 = nums[j] + play_game(i, j - 1, nums, turn + 1)
                return max(ans1, ans2)

        score = play_game(0, len(nums) - 1, nums, 1)
        return score >= 0 

