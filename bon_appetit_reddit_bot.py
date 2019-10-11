import praw
import config
from googlesearch import search

reddit = praw.Reddit(client_id=config.client_id, client_secret=config.client_secret, user_agent=config.user_agent, username=config.username, password=config.password)

subreddit = reddit.subreddit('bon_appetit')

for comment in subreddit.stream.comments():
	if "BonAppetitBot" in str(comment.body):
		recipe_name = str(comment.body).split("!")[1].strip()
		search_string = '"Bon Appetit"' + recipe_name

		for url in search(search_string, stop=3):
			if "bonappetit.com" in url:
				print(url)
				bon_appetit_url = url
				bot_response = "[{}]({})".format(recipe_name, bon_appetit_url)

				break

			else:
				bot_response = "I'm sorry, I couldn't find the right www.bonappetit.com link :("

				break

comment.reply(bot_response)