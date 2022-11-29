class Config(object):
    LOGGER = True

    API_ID = 
    API_HASH = ""
    TOKEN = ""
    OWNER_ID = 
    OWNER_USERNAME = ""
    SUPPORT_CHAT = ""
    JOIN_LOGGER = ()
    EVENT_LOGS = ()

    SQLALCHEMY_DATABASE_URI = ""
    MONGO_DB_URI = ""
    LOAD = []
    NO_LOAD = ["rss"]
    WEBHOOK = False
    INFOPIC = True
    URL = None

    ## Optional
    DRAGONS = []
    DEV_USERS = []
    DEMONS = []
    TIGERS = []
    WOLVES = []

    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = (8)
    BAN_STICKER = (
        "CAACAgUAAxkBAAEDafNhq5Z0DegqVzauwSighMw5cPWp8QACVgQAAuUG0FRXfCEuBziNzCIE"
    )
    ALLOW_EXCL = True
    CASH_API_KEY = ""
    TIME_API_KEY = ""
    BL_CHATS = []
    SPAMMERS = None
    ALLOW_CHATS = True
    START_IMG = ""
    HEROKU_API_KEY = None
    HEROKU_APP_NAME = None
    TEMP_DOWNLOAD_DIRECTORY = "./"
    ALLOW_EXCL = None
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
