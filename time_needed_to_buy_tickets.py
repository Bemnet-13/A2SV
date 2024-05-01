class Solution:
    def timeRequiredToBuy(self, tickets, k: int) -> int:
        time_req = []
        for i in range(len(tickets)):
            time = tickets[i]

            diff = time - tickets[k]
            if diff < 0:
               time_req.append(time)
            else:
                if i > k :
                    time_req.append(tickets[k] - 1)
                else:
                    time_req.append(tickets[k])

        return sum(time_req)


trial =Solution()
o = trial.timeRequiredToBuy([1,4,5,3,7], 3)
print(o)