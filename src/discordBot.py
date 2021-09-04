import random
import time
import math


from .api import API


class Bot:
  
  prefix = '[DCBOT] '
  
  email = None
  password = None
  randomRange = None
  channel = None
  token = None
  log = False
  API = API()
  
  urls = {
    'login': 'https://discord.com/api/v9/auth/login',
    'logout': 'https://discord.com/api/v9/auth/logout',
  }
  
  
  def __init__(self, email, password, channel, log = False, randomRange = 2):  
    self.randomRange = randomRange
    self.password = password  
    self.channel = channel
    self.email = email  
    self.log = log
    
  
  def sendLog(self, message):
    if (not self.log ):
      print(self.prefix + 'Logging deactivated')
      return False
    
    if (not self.token):
      print(self.prefix + 'FAILED: No session token available')
      return False

    print(self.prefix + 'Reporting to channel "' + self.log['name'] + '"...')
    self.waitRandom('Send log')
    self.API.send(self.token, self.log['id'], message)
    print(self.prefix + 'Reported to channel "' + self.log['name'] + '"')
    return True
    
  
  def sendSpam(self, content, getCooldown = True):
    print(self.prefix + 'Spamming to channel "' + self.channel['name'] + '"...')
    
    text = None
    files = None
    if (content['image']):
      files = [('file', (content['image'], open(content['image'], 'rb'), 'image/gif'))]
    if (content['text']):
      text = open(content['text'], 'r', newline='\r\n').read()
    
    self.waitRandom('Spam')
    data = self.API.send(self.token, self.channel['id'], text, files)
    if (not data['code'] == 200 and not data['code'] == 429):
      data = False
    
    i = 0
    while (not data):
      i = i + 1
      self.waitRandom('Spam (#' + str(i) + ')')
      data = self.API.send(self.token, self.channel['id'], text, files)
      if (not data['code'] == 200 and not data['code'] == 429):
        data = False
      if (i > 100):
        print(self.prefix + 'FATAL: "sendSpam" failed after 100 retrys! -> Exiting')
        exit(1)
      
    if (data['code'] == 429):
      print(self.prefix + 'Spamming failed because of too many requests (Cooldown remaining, Code: 429)')
      return {
        'success': False,
        'cooldown': self.processCool(data),
      }
    else:
      print(self.prefix + 'Spamming successful')
      if (getCooldown):
        return {
          'success': True,
          'cooldown': self.getCooldown(),
        }
    return False
  
    
  def processCool(self, data):
    if ('retry_after' in data):
      return data['retry_after']
    if ('data' in data and 'retry_after' in data['data']):
      return data['data']['retry_after']
    print(self.prefix + 'FATAL: "processCool" failed! -> Exiting')
    print(data)
    exit(1)
    
  
  def getCooldown(self):
    print(self.prefix + 'Getting cooldown for channel "' + self.channel['name'] + '"...')
    data = self.API.send(self.token, self.channel['id'], 'a')
    return self.processCool(data)
  
  
  def login(self):
    print(self.prefix + 'Logging in as "' + self.email + '"...')
    self.waitRandom('Login')
    data = self.API.login(self.urls['login'], self.email, self.password)
    
    i = 0
    while (not data):
      i = i + 1
      self.waitRandom('Login (#' + str(i) + ')')
      data = self.API.login(self.urls['login'], self.email, self.password)
      if (i > 100):
        print(self.prefix + 'FATAL: "Login" failed after 100 retrys! -> Exiting')
        exit(1)
      
    print(self.prefix + 'Logged in')
    self.token = data['token']
    return True
  
  
  def logout(self):
    print(self.prefix + 'Logging out "' + self.email + '"...')
    self.waitRandom('Logout')
    data = self.API.logout(self.urls['logout'], self.token)
    
    i = 0
    while (not data):
      i = i + 1
      self.waitRandom('Logout (#' + str(i) + ')')
      data = self.API.logout(self.urls['logout'], self.token)
      if (i > 100):
        print(self.prefix + 'FATAL: "Logout" failed after 100 retrys! -> Skipping')
        return True
      
    self.token = None
    print(self.prefix + 'Logged out')
    return True
  
  
  def waitRandom(self, forWhat):
    wait = random.randrange(self.randomRange) + 3
    print(self.prefix + 'Waiting ' + str(wait) + ' seconds to do "' + forWhat + '"')
    time.sleep(wait)
    print(self.prefix + 'Continuing')
    
    
  def doSleep(self, seconds):
    total = round(seconds)
    
    while(total >= 5):
      time_m = math.floor(total / 60)
      time_s = total - (time_m * 60)
      print(self.prefix + 'Sleep remaining: ' + str(time_m) + 'm ' + str(round(time_s)) + 's')
      total = total - 5
      time.sleep(5)
      
    print(self.prefix + 'Continuing in 5 seconds...')
    time.sleep(5)
    print('\n------\n\n')