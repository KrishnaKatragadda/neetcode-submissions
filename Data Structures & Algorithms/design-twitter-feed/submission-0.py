class Twitter:

    def __init__(self):
        self.time = 0
        self.associate = defaultdict(list) ## store the userid and associated, posts
        self.follows = defaultdict(set) ## stores the followers the user has, use set()
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.associate[userId].append([self.time,tweetId])
        self.time-=1 ## because, we need a max heap
        return
        
        

    def getNewsFeed(self, userId: int) -> List[int]:

        ##step1: check if the userId is following anyone.
        followers = self.follows.get(userId,set())
        followers.add(userId)

        ##step2: we need to get all the posts by the userid's in 
        ## followers and get the most recent 10
        res = []
        minFeed =[]
        for u in followers:
            ## check if the user has any tweets in the first place,
            ## if so we need to add them for considerataion

            if u in self.associate:
                ## get the index of the most recent tweet by the user.
                index = len(self.associate[u])-1 
                count, tweetId = self.associate[u][index]
                minFeed.append([count, tweetId,u,index-1])
        heapq.heapify(minFeed)

        while minFeed and len(res)<10:
            count, tweetId,followeeId, index = heapq.heappop(minFeed)

            res.append(tweetId)

            if index>=0:
                count, tweetId = self.associate[followeeId][index]
                heapq.heappush(minFeed, [count,tweetId, followeeId, index-1])
        
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:

        self.follows[followerId].add(followeeId)
        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
        return
        
