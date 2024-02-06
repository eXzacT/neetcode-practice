from collections import defaultdict


'''Implement the TimeMap class:

    TimeMap() Initializes the object of the data structure
    
    set(String key, String value, int timestamp)->None:
        Set stores key with the value and a timestamp
    
    get(String key, int timestamp)->str:
        Get returns the value at a given key and timestamp.
        If the key exists but timestamp doesn't then it rounds down to closest existing timestamp.
        If the key doesn't exist it returns an empty string

    Note:
        You can assume that each new set will happen at a later time, so the times will be sorted ascending'''


class TimeMap():
    def __init__(self) -> None:
        self.time_map: dict[str, list[tuple[int, str]]] = defaultdict(list)

    def __repr__(self) -> str:
        return f"<{self.time_map}>"

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, target_timestamp: int) -> str:
        if key not in self.time_map:
            return ""

        timestamps = self.time_map[key]
        last_timestamp, last_val = timestamps[-1]
        # Timestamp we're looking for is bigger than the biggest existing timestamp, return last
        if target_timestamp > last_timestamp:
            return last_val
        # Timestamp we're looking for is smaller than the smallest existing timestamp, return empty string
        first_timestamp, _ = timestamps[0]
        if target_timestamp < first_timestamp:
            return ""

        l, r = 0, len(timestamps)-1
        while l <= r:
            m = l+(r-l)//2
            timestamp, value = timestamps[m]
            if timestamp == target_timestamp:
                return value
            if timestamp < target_timestamp:
                l = m+1
            else:
                r = m-1

        # This will be the closest lower timestamp if we didn't manage to find it
        if timestamp > target_timestamp:
            return timestamps[m-1][1]
        else:
            return value
