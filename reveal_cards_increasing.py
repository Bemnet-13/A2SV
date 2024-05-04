class Solution:
    def deckRevealedIncreasing(self, deck):
        sorted_deck = sorted(deck)
        inc_deck = [-1] * len(sorted_deck)
        k = 0
        for i in range(0, len(sorted_deck), 2):
            inc_deck[i] = sorted_deck[k]
            k += 1
        

        sorted_deck[k:] = sorted(sorted_deck[k:], reverse= True)
        
        extended_queue = 2 * sorted_deck[k:]
        sorted_deck[k:] = extended_queue[1: len(sorted_deck[k:]) + 1]
        for i in range(1, len(sorted_deck), 2):
            inc_deck[i] = sorted_deck[k]
            k += 1

        return inc_deck
    
trial =Solution()
O = trial.deckRevealedIncreasing(deck = [17,13,11,2,3,5,7])
print(O)