"""
DC-Users:
dc1@scumfiction.com | Ardalrex
dc2@scumfiction.com | ItIsYeKoala

Pass: Tr5A@wPFtv
"""

import time
import requests

postTimes = {
    '01:24': 'dc1@scumfiction.com',
    '05:19': 'dc2@scumfiction.com',
    '09:21': 'dc1@scumfiction.com',
    '13:11': 'dc2@scumfiction.com',
    '17:29': 'dc1@scumfiction.com',
    '21:17': 'dc2@scumfiction.com',
}

post_channels = [
    {
        'url': 'https://discord.com/channels/837074161389142066/851024060753903628',
        'description': 'Writing State (STARTING) in own Disi.',
        'title': 'bot-msgs-state',
        'content': ' - I am going to spam now.'
    },
    {
        'url': 'https://discord.com/channels/228656196247093248/486268880575266816',
        'description': 'Spamming dcSpam in channel eu.',
        'title': 'eu',
        'content': open('dcSpam.txt', 'r', newline='\r\n').read()
    },
    {
        'url': 'https://discord.com/channels/228656196247093248/486269045298167830',
        'description': 'Spamming dcSpam in channel russia.',
        'title': 'russia',
        'content': open('dcSpam.txt', 'r', newline='\r\n').read()
    },
    {
        'url': 'https://discord.com/channels/837074161389142066/851024060753903628',
        'description': 'Writing State (DONE) in own Disi.',
        'title': 'bot-msgs-state',
        'content': ' - I am DONE spamming.'
    },
]


s = requests.Session()

loginHeaders = {
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

login = s.post(
    'https://discord.com/api/v9/auth/login',
    allow_redirects=True,
    headers=loginHeaders,
    data={
        "login": "dc2@scumfiction.com",
        "password": "Tr5A@wPFtv",
        "undelete": "false",
        "captcha_key": "null",
        "login_source": "null",
        "gift_code_sku_id": "null"
    }
)

print(login.text)
