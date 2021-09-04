#pm2 start start.py --name promo-eu --interpreter python3 -- eu
#pm2 start start.py --name promo-test --interpreter python3 -- test
#pm2 start start.py --name promo-russia --interpreter python3 -- russia

import sys
import argparse
from config import Config
from src.main import start

Conf = Config()

parser = argparse.ArgumentParser()
parser.add_argument('channel', choices=Conf.getChoices(), help='Channel to write into')
args = parser.parse_args()

start(
  auth = Conf.getAuth(),
  content = Conf.getContent(),
  log_channel = Conf.getLog(),
  spam_channel = Conf.getChannel(args.channel),
  randomSleep = Conf.getRandomSleep()
)