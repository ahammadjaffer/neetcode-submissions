from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = Counter(nums)
        count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            result.append(count[i][0])
        return result