# Program to retweet tweets based on a hashtag
from TwitterFollowBot import TwitterBot

def retweet(event):
	my_bot = TwitterBot()
	hashtag = '#' + event['hashtag']
	# autoretweets the 5(count) latest tweets that matches the hashtag
	my_bot.auto_rt(hashtag, count = 5)

def main(event):
	retweet(event)
	return {'message' : 'retweeted successfully'}