from collections import Counter
import heapq
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        sfreqs = sorted(c.values())
        ans = len(sfreqs)
        for freq in sfreqs:
            if k>=freq:
                k-=freq
                ans-=1
        return ans

#Solution with heaps
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        heap = []
        for a, b in c.items():
            heapq.heappush(heap, [b, a])
        while k > 0:
            b, a = heapq.heappop(heap)
            if b > 1:
                heapq.heappush(heap, [b - 1, a])
            k -= 1
        return len(heap)