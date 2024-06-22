def combine(n: int, k: int):
   def backtrack(first_num, path):
       if len(path) == k:
           ans.append(path[:])
           return

       for num in range(first_num, n + 1):
           path.append(num)
           backtrack(num + 1, path)
           path.pop()

   ans = []
   backtrack(1, [])
   return ans

print(combine(4, 2))