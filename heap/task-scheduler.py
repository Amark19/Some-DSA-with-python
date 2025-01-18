from collection import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], k: int) -> int:
        """
        Higher the frequency of characters more is the priority to consider it
        example
        AAAABBCC n=1
        If we consider as followes
        CBCBA idle A Idle A Idle A
        TIme = 11
        but if we start from
        ABCABACA idle A

        we can use heap here to track count and may be push the task to queue considering how
        much time should it be in queue and is first task ready to reconsider
        """
        counter_map = Counter(tasks)
        heap = [-count for count in counter_map.values()]
        heapq.heapify(heap)
        time = 0
        que = []  # (count,idle_time)
        while heap or que:
            time += 1
            if heap:
                count = 1 + heapq.heappop(heap)
                if count:
                    que.append((count, time + k))
            if que and que[0]:
                if time == que[0][1]:
                    heapq.heappush(heap, que.pop(0)[0])
        return time
