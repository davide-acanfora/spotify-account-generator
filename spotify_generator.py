import requests
import string
import random

def getRandomString(length): #Letters and numbers
    pool=string.ascii_lowercase+string.digits
    return "".join(random.choice(pool) for i in range(length))

def getRandomText(length): #Chars only
    return "".join(random.choice(string.ascii_lowercase) for i in range(length))


def main():
    print("==Spotify Account Generator==\n")
    print("Setting up..")
    nick = getRandomText(8)
    passw = getRandomString(8)
    email = nick+"@"+getRandomText(5)+".com"
    
    payload = {"creation_point": "client_mobile",
            "gender": "male",
            "birth_year": 1995,
            "displayname": nick,
            "iagree": "true",
            "birth_month": 4,
            "password_repeat": passw,
            "password": passw,
            "key": "142b583129b2df829de3656f9eb484e6",
            "platform": "Android-ARM",
            "email": email,
            "birth_day": 9}
    
    headers={"Accept-Encoding": "gzip",
             "Accept-Language": "en-US",
             "Connection": "Keep-Alive",
             "Content-Type": "Content-Type: application/x-www-form-urlencoded",
             "Host": "spclient.wg.spotify.com",
             "User-Agent": "Spotify/8.6.16 Android/22 (SM-N976N)",
             "Spotify-App-Version": "8.6.16",
             "App-Platform": "Android",
             "X-Client-Id": getRandomString(32)}

    print("Sending request..")
    r = requests.post('https://spclient.wg.spotify.com/signup/public/v1/account/', headers=headers, data=payload)

    if r.status_code==200:
        if r.json()['status']==1:
            print("Account created successfully!")
            print("Nickname: "+nick)
            print("Username: "+r.json()["username"])
            print("Password: "+passw)
            print("Email: "+email)
        else:
            print("Could not create the account.")
            print("Response error:")
            print(r.json()['errors'])
    else:
        print("Could not load the page, some errors occurred. Response code:", r.status_code)

if __name__ == "__main__":
    main()
