"""
DC-Users:
dc1@scumfiction.com | Ardalrex
dc2@scumfiction.com | ItIsYeKoala

Pass: Tr5A@wPFtv
"""

from datetime import datetime
import requests
import time
import json


#EU:
url1 = "https://discord.com/api/v9/channels/486268880575266816/messages"

#RUSSIA:
url2 = "https://discord.com/api/v9/channels/486269045298167830/messages"

#url1 = "https://discord.com/api/v9/channels/857288688168599572/messages"
#url2 = "https://discord.com/api/v9/channels/857288707728080946/messages"

#Approvement-Channel:
url3 = "https://discord.com/api/v9/channels/857320680336392223/messages"

postTimes = {
    '04:38': 'dc2@scumfiction.com',
    '10:38': 'dc1@scumfiction.com',
    '16:38': 'dc2@scumfiction.com',
    '22:38': 'dc1@scumfiction.com'
}


def sendMsg(emailAddr):
    s = requests.Session()
    lHeaders = {
        "accept": "*/*",
        "accept-language": "de",
        "content-type": "application/json",
        "sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"",
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-fingerprint": "855066585407815690.Fs9bV-nTFBITCJ81aRajKUbCics",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlLUNIIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkxLjAuNDQ3Mi4xMDYgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjkxLjAuNDQ3Mi4xMDYiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6Imh0dHBzOi8vd3d3Lmdvb2dsZS5jb20vIiwicmVmZXJyaW5nX2RvbWFpbiI6Ind3dy5nb29nbGUuY29tIiwic2VhcmNoX2VuZ2luZSI6Imdvb2dsZSIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo4Nzc4MSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=",
        "cookie": "_fbp=fb.1.1615288328555.1927512170; __dcfduid=363a041375bd31546e412ef7924c1b56; rebrand_bucket=921da5ca5ff45c190cf7571ce8ecfc27; OptanonConsent=isIABGlobal=false&datestamp=Thu+Jun+17+2021+14%3A24%3A55+GMT%2B0200+(Mitteleurop%C3%A4ische+Sommerzeit)&version=6.17.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1&AwaitingReconsent=false; locale=de"
    }

    lData = json.dumps({
        "login": emailAddr,
        "password": "Tr5A@wPFtv",
        "undelete": "false",
        "captcha_key": "null",
        "login_source": "null"
    }, separators=(',', ':'))

    login = s.post(
        'https://discord.com/api/v9/auth/login',
        allow_redirects=True,
        headers=lHeaders,
        data=lData
    )

    data = json.loads(login.text)
    token = data['token']
    theaders = {
        'Authorization': token,
        'Cookie': '__dcfduid=1e6ac93762cb42c681776b2882fdd5e5',
        'content-type': 'application/json'
    }

    tgData = json.dumps({
        'content': 'I am going to do my work now.',
        'nonce': '',
        'tts': 'false'
    }, separators=(',', ':'))

    tellGo = s.post(
        url3,
        allow_redirects=True,
        headers=theaders,
        data=tgData
    )



    headers = {
        'Authorization': token,
        'Cookie': '__dcfduid=1e6ac93762cb42c681776b2882fdd5e5',
    }
    payload = {
        'content': open('dcSpam.txt', 'r', newline='\r\n').read(),
        'nonce': '',
        'tts': 'false'
    }
    files1 = [('file', ('DisiLogo.png', open('DisiLogo.png', 'rb'), 'image/png'))]
    files2 = [('file', ('DisiLogo.png', open('DisiLogo.png', 'rb'), 'image/png'))]
    response1 = requests.request("POST", url1, headers=headers, data=payload, files=files1)
    response2 = requests.request("POST", url2, headers=headers, data=payload, files=files2)
    print('SENT FIRST MSG AT: ' + json.loads(response1.text)['timestamp'])
    print('SENT SECOND MSG AT: ' + json.loads(response2.text)['timestamp'])



    logout = s.post(
        'https://discord.com/api/v9/auth/logout',
        allow_redirects=True,
        headers=theaders,
        data=json.dumps({
            'provider': None,
            'voip_provider': None
        })
    )

    print(logout.text)

    tdData = json.dumps({
        'content': 'I am done with my work.',
        'nonce': '',
        'tts': 'false'
    }, separators=(',', ':'))

    tellDone = s.post(
        url3,
        allow_redirects=True,
        headers=theaders,
        data=tdData
    )


while True:
    time.sleep(1)
    now = datetime.now()
    dt_string = now.strftime("%H:%M")
    print('CHECKING: ' + now.strftime("%H:%M:%S"))
    if(dt_string in postTimes.keys()):
        print('SENDING MESSAGES WITH: ' + postTimes[dt_string])
        sendMsg(postTimes[dt_string])
        print('MESSAGES SENT. SLEEPING FOR ONE MINUTE...')
        time.sleep(60)
