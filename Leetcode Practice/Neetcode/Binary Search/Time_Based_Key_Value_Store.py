class TimeMap:

    def __init__(self):
        self.data = {} #key: key, value: (timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.data:
            self.data[key] = []
        self.data[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.data.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if timestamp < values[m][0]:
                r = m - 1
            else:
                l = m + 1
                res = values[m][1]

        return res
    