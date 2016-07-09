# Spotify config information
class SpotifyUser():
    SPOTIFY_MARKET="DE"
    NUMBER_OF_RELEASES_TO_LOOK_IN=10
    # To receive following information visit https://developer.spotify.com/my-applications/#!/applications
    # and register your application
    SPOTIFY_CLIENT_ID=""
    SPOTIFY_CLIENT_SECRET=""
    SPOTIFY_REDIRECT_URI=""
    SPOTIFY_USER_NAME=""

# Path to last update file
LAST_UPDATE_PATH=".lastUpdateDate"

# Twitter config information
class TwitterUser():
    # To receive following information visit https://dev.twitter.com/apps
    # and register your application
    APP_KEY = ""
    APP_SECRET = ""
    OAUTH_TOKEN = ""
    OAUTH_TOKEN_SECRET = ""