# https://neetcode.io/problems/find-the-town-judge?list=neetcode250
# EASY
# Find the Town Judge
# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly
# the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the
# person labeled bi.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        tracker = defaultdict(lambda: 0)
        amount_judge_is_trusted = n - 1
        if len(trust) == 0 and n == 1:
            return n
        for people in trust:
            trust_in = people[1]
            current = people[0]
            tracker[trust_in] += 1
            # reset if this trust anyone, so we remove at the end
            tracker[current] -= 1

        for people_key, followers_count in tracker.items():
            if followers_count == amount_judge_is_trusted:
                return people_key

        return -1

    def findJudge_minimal(self, n: int, trust: List[List[int]]) -> int:
        tracker = [0 for _ in range(0, n)]
        for people in trust:
            tracker[people[1]-1] += 1
            tracker[people[0]-1] -= 1

        for idx, followers in enumerate(tracker):
            if followers == (n - 1):
                return idx + 1
        return -1
    # def findJudge_test(self, n: int, trust: List[List[int]]) -> int:
    #     delta = defaultdict(int)

    #     for src, dst in trust:
    #         delta[src] -= 1
    #         delta[dst] += 1

    #     for i in range(1, n + 1):
    #         if delta[i] == n - 1:
    #             return i

    #     return -1


n = 4
trust = [[4, 1], [1, 2], [2, 1], [4, 2], [1, 3]]
print(Solution().findJudge(n, trust))
trust = [[1, 3], [4, 3], [2, 3]]
print(Solution().findJudge(n, trust))
n = 3
trust = [[1, 3], [2, 3], [3, 1], [3, 2]]
print(Solution().findJudge(n, trust))
n = 2
trust = [[1, 2]]
print(Solution().findJudge(n, trust))
