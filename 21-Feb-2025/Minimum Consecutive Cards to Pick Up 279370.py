# Problem: Minimum Consecutive Cards to Pick Up - https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        seen = defaultdict(int)
        min_cards = len(cards) + 1

        for end in range(len(cards)):
            if cards[end] not in seen:
                seen[cards[end]] = end
            else:
                min_cards = min(min_cards, end - seen[cards[end]] + 1)
                seen[cards[end]] = end

        return min_cards if min_cards < len(cards) + 1 else -1