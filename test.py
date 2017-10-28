# Program to retweet five latest tweets based on a hashtag (#InServerless)
from TwitterFollowBot import TwitterBot

def retweet():
	# create an instance of the TwitterFollowBot
	# by default, the bot will look for a configuration file called config.txt in your current 

	my_bot = TwitterBot()
	# autoretweets the 5(count) latest tweets that matches the hashtag
	my_bot.auto_rt("#AppleEvent", count = 5)
	return {'message' : 'retweeted successfully'}
	

retweet()


