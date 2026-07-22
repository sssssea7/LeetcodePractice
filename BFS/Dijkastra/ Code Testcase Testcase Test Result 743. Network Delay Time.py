# https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for source, target, time in times:
            graph[source].append([target, time])
        min_heap = [(0, k)]
        distance = [inf] * (n+1)
        distance[0] = distance[k] = 0
        while min_heap:
            time, node = heappop(min_heap)
            if time != distance[node]:
                continue
            for target, weight in graph[node]:
                new_time = time + weight
                if new_time < distance[target]:
                    distance[target] = new_time
                    heappush(min_heap, (new_time, target))
        mx = max(distance)
        return mx if mx!=inf else -1