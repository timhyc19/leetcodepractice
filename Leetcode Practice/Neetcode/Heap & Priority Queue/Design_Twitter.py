class Twitter:

    def __init__(self):
        self.time = 0
        self.users = defaultdict(set) # key: user, val: set of users
        self.tweets = defaultdict(set) # key: user, value: set of tweets 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].add((self.time, tweetId))
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.users[userId].add(userId)
        following = self.users[userId]
        heap = []
        res = []
        heapq.heapify(heap)
        for user in following:
            tweets = self.tweets[user]
            for tweet in tweets:
                heapq.heappush(heap, [tweet[0], tweet[1]])
        
        while heap and len(res) < 10:
            val = heapq.heappop(heap)
            res.append(val[1])

        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)