class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):return False

        s1Count = collections.defaultdict(int)
        s2Count = collections.defaultdict(int)
        for i in range(len(s1)):
            s1Count[s1[i]] += 1
            s2Count[s2[i]] += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if s1Count == s2Count:
                return True

            s2Count[s2[r]] += 1
            s2Count[s2[l]] -= 1
            if s2Count[s2[l]] == 0:
                del s2Count[s2[l]]

            l += 1

        return s1Count == s2Count