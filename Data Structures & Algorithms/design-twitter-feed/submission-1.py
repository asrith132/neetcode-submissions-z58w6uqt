from collections import deque

class Twitter:

    def __init__(self):
        self.users = set()
        self.following = defaultdict(set)
        self.tweets = defaultdict(deque)
        self.time = 0



    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users.add(userId)

        while len(self.tweets[userId]) >= 10:
            self.tweets[userId].popleft()
        
        self.tweets[userId].append((-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for tweet in self.tweets[userId]:
            heapq.heappush(heap, tweet)
        for ids in self.following[userId]:
            for tweet in self.tweets[ids]:
                heapq.heappush(heap, tweet)
        
        res = []
        for i in range(0, min(10, len(heap))):
            time, tweet = heapq.heappop(heap)
            res.append(tweet)
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users.add(followerId)
        if followeeId not in self.users:
            self.users.add(followeeId)
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
