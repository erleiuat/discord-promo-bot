from src.discordBot import Bot


prefix = '\n[MAIN] '


def logMsg(run, ch, message, line = False):
  msg = '`[' + ch + ' -> RUN ' + str(run) + ']` ' + '**' + message + '**'
  if (line):
    msg = '---\n\n' + msg 
  return msg


def run(bot, content, channel_name):
  i = 0
  cn = channel_name
  
  while True:
    i = i + 1
    
    print(prefix + '(RUN#' + str(i) + ') LOGIN:')
    bot.login()
    
    print(prefix + '(RUN#' + str(i) + ') LOGGING:')
    bot.sendLog(logMsg(i, cn, 'I successfully logged in!', True))
    
    print(prefix + '(RUN#' + str(i) + ') LOGGING:')
    bot.sendLog(logMsg(i, cn, 'I will try to send spam now...'))
    
    print(prefix + '(RUN#' + str(i) + ') SPAMMING:')
    data = bot.sendSpam(content)
    
    if (not 'cooldown' in data):
      print(prefix + '(RUN#' + str(i) + ') FATAL: No cooldown received! -> Exiting')
      exit(1)
    
    print(prefix + '(RUN#' + str(i) + ') LOGGING:')
    msg = ''
    if (data['success']):
      msg = logMsg(i, cn, 'Spam successfully sent!')
    else:
      msg = logMsg(i, cn, 'WOOOOPS: Spam __NOT__ successfully sent!')
    msg = msg + '\n'
    time_m = round((data['cooldown'] / 60) * 100) / 100
    msg = msg + logMsg(i, cn, 'I will try to logout now and try again in __' + str(time_m) + '__ minutes!')
    bot.sendLog(msg)
    
    print(prefix + '(RUN#' + str(i) + ') LOGOUT:')
    bot.logout()
    
    print(prefix + '(RUN#' + str(i) + ') SLEEP:')
    bot.doSleep(data['cooldown'])
  

def start(auth, content, log_channel, spam_channel, randomSleep = 10):
  print()
  print(prefix + 'DISCORDBOT V1.0 - Starting DiscordBot')
  bot = Bot(auth['email'], auth['password'], spam_channel, log_channel, randomSleep)
  print('----------------------------------------------------')
  run(bot, content, spam_channel['name'])