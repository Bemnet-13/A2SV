# class Solution:
#     def minimumCardPickup(self, cards: List[int]) -> int:
#         card_stack = Counter()
#         min_cards = len(cards) + 1

#         for i in range(len(cards)):
#             if cards[i] in card_stack:
#                 min_cards = min(min_cards, i - card_stack[cards[i]] + 1)  
#             card_stack[cards[i]] = i
        
#         if min_cards == len(cards) + 1:
#             return -1
#         return min_cards
    
grid = [[x,y] for x in range(4) for y in range(3)]
print(grid)
