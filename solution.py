from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrace(target, current, start):
            if target == 0:
                if current not in result:
                    result.append(current)
                return
            else:
                for i in range(start, len(candidates)):
                    if i > start and candidates[i] == candidates[i - 1]:
                        continue
                    
                    if candidates[i] > target:
                        break
                   
                    current.append(candidates[i])
                    backtrace(target - candidates[i], current[:], i + 1)
                    current.pop()

        candidates.sort()
        backtrace(target, [], 0)
        return result