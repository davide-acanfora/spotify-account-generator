# Description
This Python3 script instantly generates new free Spotify accounts (with random credentials) while pretending to be a Spotify app (currently v8.6.26) installed on an Android device. This is simply achieved by sending forged HTTP requests. The original requests have been intercepted from an emulator of a SM-N976N device running Android Lollipop, that is why you will find this particular model in the "User-Agent" header of the requests.

**Note:** I won't test this script often, so if Spotify will change their API specifications this script may not work until updated.<br>
**DISCLAIMER: by using any of the files available in this repository, you understand that you are agreeing to use at your own risk. All files available here are for education and/or research only.**

# Requirements
[requests](https://pypi.org/project/requests) module: `pip install requests`

# Usage
Simply run it without arguments to generate one account and print its credentials to the console:<br>
`python spotify_generator.py`

You can also specify the amount of accounts to generate and a file where their credentials will be saved:<br>
`python spotify_generator.py -n AMOUNT -o OUTPUT_FILE`

The creadentials will be printed/saved in the following format:<br>
`NICKNAME:USERNAME:EMAIL:PASSWORD`

# Donate
If you want to support my developments you are welcome to offer me a beer :smiley:

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/donate?business=P9UVNFTYEGTUE&currency_code=EUR)<br>
**BTC:** 1BMWGf8S9mHyaz52a85D6WRor719f6Fw5r
