class Twitter:

    def __init__(self):
        self.follows = {}
        self.tweets = {}
        self.t = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.t, tweetId))
        self.t += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        allTweets = self.tweets.get(userId, []).copy()
        for f in self.follows.get(userId, set()):
            allTweets.extend(self.tweets.get(f, []))
        allTweets.sort(reverse=True, key=lambda x:x[0])
        return [t for _, t in allTweets][:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        if followerId != followeeId: 
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].discard(followeeId)
