from datetime import datetime
import requests
import time
import json
import random


url_login = "https://discord.com/api/v9/auth/login"
url_logout = "https://discord.com/api/v9/auth/logout"
password = "Tr5A@wPFtv"

#eu		    486268880575266816
#russia	    486269045298167830
#asia	    486268997633966090
#_update    857320680336392223



chInfo = {
    'eu': {
        'name': '#EU',
        'channel': '486268880575266816',
        'content': 'dcSpam_eu.txt',
        'image': True
    },
    'russia': {
        'name': '#RUSSIA',
        'channel': '486269045298167830',
        'content': 'dcSpam_russia.txt',
        'image': True
    },
    'asia': {
        'name': '#ASIA',
        'channel': '486268997633966090',
        'content': 'dcSpam_asia.txt',
        'image': False
    },
    'update': {
        'name': '#promo-bot-work',
        'channel': '857320680336392223',
        'content': None,
        'image': False
    }
}



postTimes = {
    'eu': {
        '10:35': 'dc2@scumfiction.com',
        '16:35': 'dc1@scumfiction.com',
        '22:35': 'dc2@scumfiction.com'
    },
    'russia': {
        '09:35': 'dc2@scumfiction.com',
        '15:35': 'dc1@scumfiction.com',
        '21:35': 'dc2@scumfiction.com'
    },
    'asia': {
        '06:35': 'dc10@scumfiction.com'
    }
}



def sendLogin(mail): 
    print('[AUTH] -> LOGGING IN')

    login = requests.post(
        url_login,
        allow_redirects = True,
        headers = {
            "accept": "*/*",
            "content-type": "application/json"
        },
        data = json.dumps({
            "login": mail,
            "password": password,
            "undelete": "false",
            "captcha_key": "null",
            "login_source": "null"
        }, separators=(',', ':'))
    )

    data = json.loads(login.text)

    if('token' in data.keys()):
        print('[AUTH] -> LOGIN SUCCESSFUL')
        return data['token']
    else:
        print('[AUTH] -> LOGIN FAILED')
        return False



def sendLogout(token):
    print('[AUTH] -> LOGGING OUT')

    logout = requests.post(
        url_logout,
        allow_redirects = True,
        headers = {
            "accept": "*/*",
            "content-type": "application/json",
            'Authorization': token
        },
        data = json.dumps({
            'provider': None,
            'voip_provider': None
        })
    )

    if(not logout.text):
        print('[AUTH] -> LOGOUT SUCCESSFUL')
        return True
    else:
        print('[AUTH] -> LOGOUT PROBABLY UNSUCCESSFUL')
        return False



def sendMessage(ch, token, content):
    print('\n[MSGS] -> SENDING MESSAGE TO "'+ch['name']+'"')

    if(ch['image']):
        files = [('file', ('DisiLogo.png', open('DisiLogo.png', 'rb'), 'image/png'))]
    else:
        files = None

    response = requests.request(
        "POST", 
        "https://discord.com/api/v9/channels/"+ch['channel']+"/messages",
        headers={
            'Authorization': token
        },
        data={
            'content': content,
            'nonce': '',
            'tts': 'false'
        },
        files=files
    )

    if(not isinstance(response.text, str) and 'timestamp' in response.text.keys()):
        print('[MSGS] -> SENT MESSAGE AT: ' +
            json.loads(response.text)['timestamp'] + '\n')
    else:
        print(response.text)
    



def randomSleep():
    randomSleep = random.randint(2, 17)
    print('[SLEEP] -> WAITING FOR ' + str(randomSleep) + ' MINUTES BEFORE SENDING...')
    time.sleep(randomSleep*60/2)
    print('[SLEEP] -> HALF WAY THERE...')
    time.sleep(randomSleep*60/2)
    print('[SLEEP] -> CONTINUING')



def doIt(mail, ch):
    print('\n[MSGS] -> SENDING MESSAGES WITH "'+mail+'" TO "'+ch['name']+'"\n')
    randomSleep()
    token = sendLogin(mail)
    sendMessage(chInfo['update'], token, 'I am going to do my work now in **' + ch['name'] + '**')
    time.sleep(2)
    sendMessage(ch, token, open(ch['content'], 'r', newline='\r\n').read())
    time.sleep(2)
    sendMessage(chInfo['update'], token, 'I am done.')
    sendLogout(token)
    time.sleep(2)
    print('\n[MSGS] -> MESSAGES SENT\n')


while True:
    time.sleep(5)

    now = datetime.now()
    dt_string = now.strftime("%H:%M")
    print('[CHECKING] -> ' + now.strftime("%H:%M:%S"))

    if(dt_string in postTimes['eu'].keys()):
        doIt(postTimes['eu'][dt_string], chInfo['eu'])

    elif(dt_string in postTimes['russia'].keys()):
        doIt(postTimes['russia'][dt_string], chInfo['russia'])

    elif(dt_string in postTimes['asia'].keys()):
        doIt(postTimes['asia'][dt_string], chInfo['asia'])
