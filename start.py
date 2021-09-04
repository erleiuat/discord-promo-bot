#pm2 start start.py eu --name promo-eu --interpreter python3
#pm2 start start.py test --name promo-test --interpreter python3
#pm2 start start.py russia --name promo-russia --interpreter python3

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
)