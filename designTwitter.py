from collections import defaultdict

class Twitter:
    
    def __init__(self):
        self.followingMap = defaultdict(lambda: set())
        self.tweets = []
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId,tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        for uID, tID in reversed(self.tweets):
            if uID in self.followingMap[userId] or userId == uID:
                feed.append(tID)
            if len(feed) == 10: break
        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followingMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followingMap[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
