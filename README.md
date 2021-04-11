# Description
This Python3 script instantly generates a new Spotify account (with random credentials) pretending to be an older Spotify app (v8.4.38) on an Android device. This is simply achieved by sending forged HTTP requests. The original requests have been intercepted from an old GT-P7500, that is why you will find this particular model in the User-Agent of the requests.

**Note:**  I won't test this script often, so if Spotify will change their API specifications this script may not work until updated.

# Requirements
"requests" module: `pip install requests`

# Usage
Simply run it using Python3<br>
`python spotify_generator.py`
