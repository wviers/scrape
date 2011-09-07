import json
import httplib


def find_messages(name, tweets):
    conn = httplib.HTTPConnection("www.twitter.com")
    tweet_strings = []
    iterations = 0

    print "searching ", name
    print ""

    conn.request("GET", "/statuses/user_timeline.json?screen_name=" + name + "&count= " + tweets)
    r1 = conn.getresponse()
    print r1.status, r1.reason
    data1 = r1.read()
 
    data2 = json.loads(data1)
    print ""

    while iterations < int(tweets):
        tweet_strings.append(data2[iterations]['text'])
        iterations = iterations + 1

    conn.close
    return tweet_strings


name = raw_input("Enter a twitter user:")
times = raw_input("Enter a number of tweets:")

messages = find_messages(name, times) 

count = 0
while count < int(times):
    print messages[count]
    count = count + 1
     

