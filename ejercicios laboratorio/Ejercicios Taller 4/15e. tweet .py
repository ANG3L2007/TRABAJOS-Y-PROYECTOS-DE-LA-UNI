def Hashtag(tweet):
    pos = tweet.find("#")
    if pos == -1:
        return 0
    hashtag = ""
    pos += 1
    while pos < len(tweet) and tweet[pos] != " ":
        hashtag += tweet[pos]
        pos += 1
    return hashtag

"""The earth is about to reach a point of no return #SOSClimateChange"""


tweet = input("ingrese el tweet ")
print(Hashtag(tweet))