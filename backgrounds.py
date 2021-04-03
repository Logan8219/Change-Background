import praw
from random import randint
import urllib.request
import ctypes


# Login Details
reddit = praw.Reddit(
	client_id = 'nyCob32A14KKRw',
	client_secret = 'iZrXu3xdl-ptgkmoDB0goFaVc07GsQ',
	user_agent = 'Backround image bot by Minute_Race_4554'
	)
#Making a random number
x = randint(2,19)

# Getting the URL for the image
sub = reddit.subreddit('earthporn')
posts = [post for post in sub.hot(limit=20)]
rand_post = posts[x]
url = rand_post.url

#Download the image
urllib.request.urlretrieve(url, 'image.jpg')

#Set image as background

directory = 'c:\Programming\Backgrounds\image.jpg'

SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, directory , 0)
