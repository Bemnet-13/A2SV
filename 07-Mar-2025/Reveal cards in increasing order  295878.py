# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        q = deque([i for i in range(len(deck))])
        deck.sort()

        ans = [0] * len(deck)
        i = 0

        while len(q) > 0:
            index = q.popleft()
            ans[index] = deck[i]
            if q:
                new_index = q.popleft()
                q.append(new_index)
            i += 1
        
        return ans
