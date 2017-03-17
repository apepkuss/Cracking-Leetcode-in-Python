
class Twitter(object):
    """
    @ Amazon, Twitter

    Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to
    see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

    1. postTweet(userId, tweetId): Compose a new tweet.
    2. getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed
    must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to
    least recent.
    3. follow(followerId, followeeId): Follower follows a followee.
    4. unfollow(followerId, followeeId): Follower unfollows a followee.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = {}
        self.followees = {}
        self.followers = {}
        self.order = 0


    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.order += 1
        tweet = (userId, tweetId, self.order)
        # update your own tweets stack
        if userId in self.tweets:
            self.tweets[userId].append(tweet)
        else:
            self.tweets[userId] = [tweet]

        # update your followers' tweets stack
        if userId in self.followers:
            for follower in self.followers[userId]:
                if follower in self.tweets:
                    self.tweets[follower].append(tweet)
                else:
                    self.tweets[follower] = [tweet]


    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by
        users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if userId in self.tweets:
            if len(self.tweets[userId]) > 10:
                tweets = self.tweets[userId][len(self.tweets[userId] ) -10:]
            else:
                tweets = self.tweets[userId]
            return [tweet for _, tweet, _ in tweets][::-1]
        return []



    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId:
            return
        # update the followee list of current follower
        if followerId in self.followees:
            if followeeId not in self.followees[followerId]:
                self.followees[followerId].append(followeeId)
                self._updateTweets(followerId, followeeId)
        else:
            self.followees[followerId] = [followeeId]
            self._updateTweets(followerId, followeeId)

        # update the follower list of current followee
        if followeeId in self.followers:
            if followerId not in self.followers[followeeId]:
                self.followers[followeeId].append(followerId)
        else:
            self.followers[followeeId] = [followerId]

    def _updateTweets(self, followerId, followeeId):
        # udpate the follower's tweets list
        if followerId in self.tweets:
            if followeeId in self.tweets:
                follower_tweets = self.tweets[followerId]
                followee_tweets = self.tweets[followeeId]
                i, j = 0, 0
                new_tweets = []
                while i< len(follower_tweets) and j < len(followee_tweets):
                    if followee_tweets[j][0] != followeeId:
                        j += 1
                        continue
                    if follower_tweets[i][2] <= followee_tweets[j][2]:
                        new_tweets.append(follower_tweets[i])
                        i += 1
                    else:
                        new_tweets.append(followee_tweets[j])
                        j += 1
                if i < len(follower_tweets):
                    new_tweets += follower_tweets[i:]
                elif j < len(followee_tweets):
                    while j < len(followee_tweets):
                        if followee_tweets[j][0] == followeeId:
                            new_tweets.append(followee_tweets[j])
                        j += 1
                self.tweets[followerId] = new_tweets
        elif followeeId in self.tweets:
            self.tweets[followerId] = []
            i = 0
            while i < len(self.tweets[followeeId]):
                if self.tweets[followeeId][i][0] == followeeId:
                    self.tweets[followerId].append(self.tweets[followeeId][i])
                i += 1
        else:
            self.tweets[followerId] = []

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId:
            return

        # update the followee list of current follower
        if followerId in self.followees:
            if followeeId in self.followees[followerId]:
                self.followees[followerId].remove(followeeId)

        # update the follower list of current followee
        if followeeId in self.followers:
            if followerId in self.followers[followeeId]:
                self.followers[followeeId].remove(followerId)

        # update the follower's tweets list
        if followerId in self.tweets:
            self.tweets[followerId] = [tweet for tweet in self.tweets[followerId] if tweet[0] != followeeId]



    # Your Twitter object will be instantiated and called as such:
    # obj = Twitter()
    # obj.postTweet(userId,tweetId)
    # param_2 = obj.getNewsFeed(userId)
    # obj.follow(followerId,followeeId)
    # obj.unfollow(followerId,followeeId)