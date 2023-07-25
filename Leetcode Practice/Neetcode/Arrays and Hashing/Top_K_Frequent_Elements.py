class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        d = [[] for i in range(len(nums) + 1)]
        res = []
        for key, value in c.items():
            d[value].append(key)
        

        for i in range(len(d)-1, -1, -1):
            for val in d[i]:
                res.append(val)
                if len(res) == k:
                    return res
            