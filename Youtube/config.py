
import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7258053065:AAEW4EipYpSkA070iJMLeNgKF9RARRVKHi8")
    API_ID = int(os.environ.get("API_ID",27317669 ))
    API_HASH = os.environ.get("API_HASH", "11b88c331c5d44fde57cf91de1a2156b")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "-1002578602154")
    MUSIC_CHANNEL = int(os.environ.get("MUSIC_CHANNEL", "-1002578602154"))
    OWNER = os.environ.get("OWNER", "6947378236")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
