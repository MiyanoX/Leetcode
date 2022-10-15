class TimeMap:

    def __init__(self):
        self.items = {}          

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.items:
            self.items[key][timestamp] = value
        else:
            self.items[key] = {timestamp: value}

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.items:
            return ""
        dict = self.items[key]
        i = timestamp
        while i > 0:
            if i in dict:
                return dict[i]
            else:
                i -= 1
        return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)