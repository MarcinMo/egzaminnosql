import time
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['nosql']
collection = db.reddit2

def measureTime(a):
    start = time.clock()
    a()
    elapsed = time.clock()
    elapsed = elapsed - start
    print "Time spent in executing function %s is: %s" % (a.__name__, elapsed)

def agr1():
    x = collection.aggregate(
       [
          { "$unwind" : "$subreddit"}, { "$sortByCount": "$subreddit" }
       ]
    )
    # for i in list(x):
    #     print i

def agr2():
    x = collection.aggregate(
       [
           { "$match" :{"subreddit" : "AskReddit" }},
           { "$group" : {"_id": None, "count": {"$sum": 1}}}
       ]
    )
    # print list(x)

def agr3():
    x = collection.aggregate(
        [
            {"$match": {"downs": {"$gt": 0}}},
            {"$group": {"_id": None, "count": {"$sum": 1}}}
        ]
    )
    print list(x)

def agr4():
    x = collection.aggregate(
        [
            {"$match": {"subreddit": "AskReddit"}},
            {"$sort": {"ups": -1}},
            {"$limit": 10}
        ]
    )
    # for i in list(x):
    #     print i

for i in xrange(1,5):
    print'-' * 30
    print "Agregacja %d:" %i
    eval("measureTime(agr%d)"%i)
