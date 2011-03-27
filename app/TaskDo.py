from flaskext.twython import Twython

def ReturnWeeklyTrends():
	twitter = Twython()
	trends=twitter.getWeeklyTrends()
	return trends

