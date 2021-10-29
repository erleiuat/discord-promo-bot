class Config:
  
  email = '...'
  password = '...'
  
  spam_text = 'data/spam.txt'
  spam_image = 'data/logo.gif'
  
  randomSleep = 5
  
  channel_log = {
    'name': '#promo-bot-log',
    'id': '857320680336392223',
  }
  
  channels_spam = {
    'test': {
      'name': '#testing',
      'id': '869134193748234291',
    },
    'russia': {
      'name': '#RUSSIA',
      'id': '486269045298167830',
    },
    'eu': {
      'name': '#EU',
      'id': '486268880575266816',
    }
  }
  
  
  def getChoices(self):
    return self.channels_spam.keys()
  
  
  def getAuth(self):
    return {
      'email': self.email,
      'password': self.password,
    }
    
    
  def getContent(self):
    return {
      'text': self.spam_text,
      'image': self.spam_image,
    }
    
    
  def getLog(self):
    return {
      'name': self.channel_log['name'],
      'id': self.channel_log['id'],
    }
    
    
  def getChannel(self, selection):
    return self.channels_spam[selection]
  
  
  def getRandomSleep(self):
    return self.randomSleep
  
  
#eu			486268880575266816
#russia		486269045298167830
#asia		486268997633966090
#us-east	486268909113311242
#us-west	486268938137632768
#_update    857320680336392223
#testing	869134193748234291
