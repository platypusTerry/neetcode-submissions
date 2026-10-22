class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps = {}
        heap = []

        for n in nums: # O(n)
            maps[n] = maps.get(n,0) + 1
        
        for num, count in maps.items(): # O(k), k表有幾個不同的數字
            heapq.heappush(heap, (-count, num)) # O(logk)
            #heapq.heappush(放進哪個 heap, (要放什麼))
            #(要放什麼)：第一個跟第二個參數是誰先被拿來比較

        answer = []
        for i in range(k):
            count, num = heapq.heappop(heap)
            #也可用 _, num = heapq.heappop(heap) 因為count用不到
            answer.append(num)
        
        return answer