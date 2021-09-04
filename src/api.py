import requests
import json


class API:

  prefix = '[API] '
  
  
  def send(self, token, channel, content, files = None):
    print(self.prefix + 'Sending Message...')
    
    response = requests.request(
      'POST', 
      'https://discord.com/api/v9/channels/' + channel + '/messages',
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
    
    if (response.status_code == 200):
      print(self.prefix + 'Successfully sent message (Code: 200)')
      try:
        data = json.loads(response.text)
        return {
          'code': response.status_code,
          'data': data,
        }
      except ValueError as e:
        return True
      
    print(self.prefix + 'Sending failed (Code: ' + str(response.status_code) + ')')
    try:
      data = json.loads(response.text)
      return {
        'code': response.status_code,
        'data': data,
      }
    except ValueError as e:
      return False
    
  
  def login(self, url, email, password):
    print(self.prefix + 'Sending Login request...')
    
    response = requests.post(
      url,
      allow_redirects = True,
      headers = {
        'accept': '*/*',
        'content-type': 'application/json'
      },
      data = json.dumps({
        'login': email,
        'password': password,
        'undelete': 'false',
        'captcha_key': 'null',
        'login_source': 'null'
      }, separators=(',', ':'))
    )
    
    data = json.loads(response.text)
    
    if (not 'token' in data):
      print(self.prefix + 'Login failed:')
      print(data)
      return False
    
    print(self.prefix + 'Login successful!')
    return data
    
    
  def logout(self, url, token):
    print(self.prefix + 'Sending Logout request...')
    
    response = requests.post(
      url,
      allow_redirects = True,
      headers = {
        'accept': '*/*',
        'content-type': 'application/json',
        'Authorization': token
      },
      data = json.dumps({
        'provider': None,
        'voip_provider': None
      })
    )
    
    if (response.status_code == 204):
      return True

    print(self.prefix + 'Logout failed with code: ' + str(response.status_code)) 
    return True
    
    