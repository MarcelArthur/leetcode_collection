from collections import OrderedDict
# 维持一个公共序列并且记录每一次入组的是将顺序，同时用userlist记录入组信息对应的用户信息
# 不然发布的时候打上时间戳之后进行排序处理？会出现大量空间占用和时间消耗
# 没有AC，没有解决记录每个用户发帖顺序的问题(时间戳？索引标记？)，此时这里需要一个发帖同步纪录的队列？
# class Twitter:
#     result = deque()
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.twitter = OrderedDict()
#         self.user_list = dict()

#     def postTweet(self, userId, tweetId):
#         """
#         Compose a new tweet.
#         :type userId: int
#         :type tweetId: int
#         :rtype: void
#         """
#         self.twitter[userId] = self.twitter.get(userId, [])
#         self.twitter.get(userId).append(tweetId)
        

#     def getNewsFeed(self, userId):
#         """
#         Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
#         :type userId: int
#         :rtype: List[int]
#         """
#         # 先过滤用户关注列表并在之后拼接用户user_ID_list
#         # 因为关注时间没有明确的先后顺序
#         # 取交集
#         result = []
#         user_one_set = set(self.user_list.get(userId, []))
#         twitter_set = {x for x in self.twitter.keys()}
#         intersection = twitter_set.intersection(user_one_set)
#         order_twitter_key = [x for x in self.twitter.keys()][::-1]
#         for one_twitter in order_twitter_key:
#             if one_twitter == userId or one_twitter in intersection:
#                 result.extend(self.twitter.get(one_twitter)[::-1])
        
#         if not result:
#             resutl = None
#         return result[:10]
        

#     def follow(self, followerId, followeeId):
#         """
#         Follower follows a followee. If the operation is invalid, it should be a no-op.
#         :type followerId: int
#         :type followeeId: int
#         :rtype: void
#         """
#         self.user_list[followerId] = self.user_list.get(followerId, [])
#         self.user_list.get(followerId).append(followeeId)
        

#     def unfollow(self, followerId, followeeId):
#         """
#         Follower unfollows a followee. If the operation is invalid, it should be a no-op.
#         :type followerId: int
#         :type followeeId: int
#         :rtype: void
#         """
#         if followeeId in set(self.user_list.get(followerId, [])):
#             self.user_list.get(followerId).remove(followeeId)
#         print(self.user_list.get(followerId))
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

# 处理获取长度为10的Feed流方式为在其中设计一个(value, index)的元组，通过标记索引的方式获取到发推顺序
# https://www.hrwhisper.me/leetcode-design-twitter/
class Twitter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets_cnt = 0
        self.tweets = collections.defaultdict(list)
        self.follower_ship = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.tweets[userId].append([tweetId, self.tweets_cnt])
        self.tweets_cnt += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        recent_tweets = []
        user_list = list(self.follower_ship[userId]) + [userId]
        userId_tweet_index = [[userId, len(self.tweets[userId]) - 1] for userId in user_list if userId in self.tweets]

        for _ in range(10):
            max_index = max_tweet_id = max_user_id = -1
            for i, (user_id, tweet_index) in enumerate(userId_tweet_index):
                if tweet_index >= 0:
                    tweet_info = self.tweets[user_id][tweet_index]
                    if tweet_info[1] > max_tweet_id:
                        max_index, max_tweet_id, max_user_id = i, tweet_info[1], user_id

            if max_index < 0: break
            recent_tweets.append(self.tweets[max_user_id][userId_tweet_index[max_index][1]][0])
            userId_tweet_index[max_index][1] -= 1

        return recent_tweets

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId != followeeId:
            self.follower_ship[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.follower_ship and followeeId in self.follower_ship[followerId]:
            self.follower_ship[followerId].remove(followeeId)

            
# Top Solution
# 使用堆处理Feed
# 来源: LeetCode Accepted Solutions Runtime Distribution Top 1
from heapq import *

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 0
        self.userTweets = {}
        self.userFollowers = {}
        

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId in self.userTweets:
            self.userTweets[userId].append((tweetId, self.time))
        else:
            self.userTweets[userId] = [(tweetId, self.time)]
            
        self.time += 1
       

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        heap, ans = [], []
        feeders = [userId] if userId not in self.userFollowers else list(self.userFollowers[userId]) + [userId]
        
        for f in feeders:
            if f in self.userTweets:
                tweets = self.userTweets[f]
                if len(tweets) > 0:
                    heappush(heap, (-tweets[-1][1], tweets[-1][0], len(tweets) - 1, tweets))
        
        while len(ans) < 10 and len(heap) > 0:
            t, tweetId, idx, tweets = heappop(heap)
            ans.append(tweetId)
            if idx > 0:
                heappush(heap, (-tweets[idx-1][1], tweets[idx-1][0], idx - 1, tweets))
                
        return ans

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId:
            return
        
        if followerId in self.userFollowers:
            self.userFollowers[followerId].add(followeeId)
        else:
            self.userFollowers[followerId] = set([followeeId])
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.userFollowers and followeeId in self.userFollowers[followerId]:
            self.userFollowers[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
