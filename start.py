"""
DC-Users:
dc1@scumfiction.com | Ardalrex
dc2@scumfiction.com | ItIsYeKoala

Pass: Tr5A@wPFtv
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time

postTimes = {
    '12:10': 'dc1@scumfiction.com',
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
        'url': 'https://discord.com/channels/837074161389142066/851024060753903628',
        'description': 'Spamming dcSpam in channel eu.',
        'title': 'eu',
        'content': open('dcSpam.txt', 'r', newline='\r\n').read()
    },
    {
        'url': 'https://discord.com/channels/837074161389142066/851024060753903628',
        'description': 'Spamming dcSpam in channel russia.',
        'title': 'eu',
        'content': open('dcSpam.txt', 'r', newline='\r\n').read()
    },
    {
        'url': 'https://discord.com/channels/837074161389142066/851024060753903628',
        'description': 'Writing State (DONE) in own Disi.',
        'title': 'bot-msgs-state',
        'content': ' - I am DONE spamming.'
    },
]


def login(driver, email):
    time.sleep(0.5)
    driver.get('https://discord.com/login')
    time.sleep(1)
    if "Discord" in driver.title:
        elem = driver.find_element_by_name("email")
        elem.clear()
        elem.send_keys(email)
        elem = driver.find_element_by_name("password")
        elem.clear()
        elem.send_keys("Tr5A@wPFtv")
        time.sleep(0.5)
        elem.send_keys(Keys.RETURN)


def writeSpam(driver, content):
    elem = driver.find_element_by_xpath(
        '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div[2]')
    data = content
    elem.send_keys(data[::-1])
    elem.send_keys(Keys.RETURN)


def timeToSpam(user):
    print('Spamming as: ' + user)
    driver = webdriver.Firefox()
    login(driver, user)

    for i in post_channels:
        print('Doing: ' + i['description'])
        time.sleep(1)
        driver.get(i['url'])
        time.sleep(1)
        if(not (i['title'] in driver.title)):
            print('UNABLE TO ACCESS CORRECT TEXTCHAT')
            time.sleep(5)
        else:
            writeSpam(driver, i['content'])
            time.sleep(5)

    print('DONE Spamming as: ' + user)
    time.sleep(185)
    driver.close()
    time.sleep(10)


while(True):
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print(current_time)
    if(current_time in postTimes):
        print(current_time + ': Posting-Time!')
        timeToSpam(postTimes[current_time])
    time.sleep(15)
