class TimeMap:

    def __init__(self):
        # {"key1": [(value1, timestamp1),(value1, timestamp2)]}
        self.hash_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.hash_map.get(key):
            self.hash_map[key].append((value, timestamp))
        else:
            self.hash_map[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if not self.hash_map.get(key):
            return ""
        all_values = self.hash_map[key]
        sorted_ts = sorted(all_values, key=lambda x: x[1])
        # Search for most recent timestamp
        l = 0
        r = len(all_values)
        print(l, r, sorted_ts)
        
        while(l < r):
            m = (l+r)//2
            if sorted_ts[m][1] > timestamp:
                r = m
            else:
                l = m+1
        
        return sorted_ts[r-1][0] if (sorted_ts[r-1][1] <= timestamp) else ""
