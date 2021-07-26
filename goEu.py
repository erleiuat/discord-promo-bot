from datetime import datetime
import requests
import random
import time
import json


url_login = "https://discord.com/api/v9/auth/login"
url_logout = "https://discord.com/api/v9/auth/logout"
password = "Tr5A@wPFtv"

#eu			486268880575266816
#russia		486269045298167830
#asia		486268997633966090
#us-east	486268909113311242
#us-west	486268938137632768
#_update    857320680336392223
#testing	869134193748234291



chInfo = {
    'eu': {
        'name': '#EU',
        'channel': '486268880575266816',
        'content': 'dcSpam_default.txt',
        'image': True
    },
    'us-east': {
        'name': '#US-EAST',
        'channel': '486268909113311242',
        'content': 'dcSpam_default2.txt',
        'image': False
    },
    'us-west': {
        'name': '#US-WEST',
        'channel': '486268938137632768',
        'content': 'dcSpam_default2.txt',
        'image': False
    },
    'russia': {
        'name': '#RUSSIA',
        'channel': '486269045298167830',
        'content': 'dcSpam_default.txt',
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

    data = json.loads(response.text)
    if(not isinstance(data, str) and 'timestamp' in data.keys()):
        print('[MSGS] -> SENT MESSAGE AT: ' +
              data['timestamp'] + '\n')
        return True
    else:
        print(response.text)
        return False
    



def randomSleep():
    randomSleep = random.randint(2, 15)
    print('[SLEEP] -> WAITING FOR ' + str(randomSleep) + ' MINUTES BEFORE SENDING...')
    for x in range(randomSleep):
        print('[SLEEP] -> '+str(randomSleep-x)+' REMAINING...')
        time.sleep(60)
    print('[SLEEP] -> DONE: CONTINUING')



def doIt(mail, ch, token):
    print('\n[MSGS] -> SENDING MESSAGES WITH "'+mail+'" TO "'+ch['name']+'"\n')
    
    sendMessage(chInfo['update'], token, 'I am going to do my work now in **' + ch['name'] + '**')
    time.sleep(1)
    success = sendMessage(ch, token, open(ch['content'], 'r', newline='\r\n').read())
    time.sleep(1)
    if(success):
        sendMessage(chInfo['update'], token, 'I am done.')
    else:
        sendMessage(chInfo['update'], token, 'I am done but it was **unsuccessful**.')
    
    time.sleep(1)
    print('\n[MSGS] -> MESSAGES SENT\n')

def longSleep(total = 6 * 60 * 60 + 120):
    while(total > 0):
        print('[SLEEP] -> Remaining: ' + str(round(total / 60)) + ' min')
        total = total - 10
        time.sleep(10)


while True:
    email = 'dc1@scumfiction.com'
    token = sendLogin(email)
    doIt(email, chInfo['eu'], token)
    sendLogout(token)
    longSleep()
