import heapq

class TimeMap:

    def __init__(self):
        # {"key1": [(timestamp1, value1), (timestamp2, value2)]}
        self.hash_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash_map.keys():
            self.hash_map[key] = []
        
        heapq.heappush(self.hash_map[key], (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.hash_map.get(key):
            return ""
        sorted_ts = self.hash_map[key]
        # sorted_ts = sorted(all_values, key=lambda x: x[1])
        # Search for most recent timestamp
        l = 0
        r = len(sorted_ts)
        
        while(l < r):
            m = (l+r)//2
            if sorted_ts[m][0] > timestamp:
                r = m
            else:
                l = m+1
        
        return sorted_ts[r-1][1] if (sorted_ts[r-1][0] <= timestamp) else ""
