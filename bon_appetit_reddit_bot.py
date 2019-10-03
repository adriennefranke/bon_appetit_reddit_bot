import praw
import config

r = praw.Reddit(client_id=config.client_id, client_secret=config.client_secret, user_agent=config.user_agent, username=config.username, password=config.password)

subreddit = r.subreddit('bon_appetit')

comments = subreddit.stream.comments()

for comment in comments:
	print(str(comment.body))

# UA = 'bon appetit subreddit recipe bo. contact me at /u/adriennefranke or adri.j.franke@gmail.com'
# r = praw.Reddit(UA)


# for c in praw.helpers.comment_stream(r, 'bon_appetit'):
# 	if check_condition(c):
# 		bot_action(c)