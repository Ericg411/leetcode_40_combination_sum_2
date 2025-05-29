from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrace(target, current, start):
            if target == 0:
                current.sort()
                if current not in result:
                    result.append(current)
                return
            else:
                for i in range(start, len(candidates)):
                    if candidates[i] > target:
                        continue
                    else:
                        current.append(candidates[i])
                        backtrace(target - candidates[i], current[:], i + 1)
                        current.pop()

        backtrace(target, [], 0)
        return result