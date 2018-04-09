import requests
import string
import random

def getRandomString(length): #Letters and numbers
    pool=string.ascii_lowercase+string.digits
    return "".join(random.choice(pool) for i in range(length))

def getRandomText(length): #Chars only
    return "".join(random.choice(string.ascii_lowercase) for i in range(length))

print("==Spotify Account Generator by dadeaka==\n")

print("Setting up..")
user = getRandomText(8)
passw = getRandomString(8)
email = user+"@"+getRandomText(5)+".com"
payload = {"creation_point": "client_mobile",
        "gender": "male",
        "postal_code": 1,
        "birth_year": 1995,
        "username": user,
        "iagree": 1,
        "birth_month": 4,
        "password_repeat": passw,
        "password": passw,
        "invitecode": "",
        "key": "142b583129b2df829de3656f9eb484e6",
        "platform": "Android-ARM",
        "email": email,
        "birth_day": 9,
        "creation_flow": "client_mobile"}
headers={"Accept-Encoding": "gzip",
         "Accept-Language": "it-IT;q=1, en-US;q=0.5",
         "Connection": "Keep-Alive",
         "Content-Type": "application/x-www-form-urlencoded",
         "Host": "www.spotify.com",
         "User-Agent": "Spotify/8.4.38 Android/25 (GT-P7500)"}

print("Sending request..")
r = requests.post('https://www.spotify.com/int/xhr/json/sign-up/', headers=headers, data=payload)

if r.status_code==200:
    if r.json()['status']==1:
        print("Account created successfully!")
        print("User: "+user)
        print("Password: "+passw)
        print("Email: "+email)
    else:
        print("Could not create the account.")
        print("Response error:")
        print(r.json()['errors'])
else:
    print("Could not load the page, some errors occurred. Response code:", r.status_code)
