class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 0:
            num_lst = list(str(num))
            num_lst.pop(0)
            num_lst.sort(reverse= True)
            return -1 * int("".join(num_lst))
        else:
            num_lst = list(str(num))
            num_lst.sort()
            if num_lst[0] != "0" or (num_lst[0] == "0" and len(num_lst) == 1):
                return int("".join(num_lst))
            else:
                for i in range(len(num_lst)):
                    if num_lst[i] != "0":
                        num_lst[0], num_lst[i] = num_lst[i], num_lst[0]
                        break
                return int("".join(num_lst))

                