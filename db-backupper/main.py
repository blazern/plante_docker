import argparse
import logging
import os
import sys
import time
import subprocess

from datetime import datetime
from datetime import date
from datetime import timedelta

def check_call(cmd):
  logging.info('Executing cmd: {}\n'.format(cmd))
  subprocess.check_call(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

def main(argv):
  parser = argparse.ArgumentParser()
  parser.add_argument('--out-folder', required=True,
                      help='Folder which will be used to store the outputs')
  parser.add_argument('--psql-url', required=True,
                      help='Url to connect to DB. Example: '
                      + 'postgresql://main_user:cunning_password@localhost/main')
  parser.add_argument('--when', required=True,
                      help='At what time of day to make screenshots. '
                      + 'Format: hh:mm (e.g. 13:30)')
  options = parser.parse_args()

  logging.getLogger().setLevel(logging.DEBUG)
  logging.info('Args: {}'.format(options))

  if not os.path.exists(options.out_folder):
    logging.info('Out folder {} doesn\'t exist. Creating it.'
      .format(options.out_folder))
    os.makedirs(options.out_folder)

  while (True):
    today_str = date.today().strftime('%d.%m.%Y')
    next_backup_time = datetime.strptime(
      '{} {}'.format(today_str, options.when),
      '%d.%m.%Y %H:%M')

    now = datetime.now()
    sleep_time = (next_backup_time - now).total_seconds()
    if sleep_time > 0:
      logging.info('Now: ({}), next backup time: ({}), sleeping for {} seconds'
        .format(now, next_backup_time, sleep_time))
      time.sleep(sleep_time)

    check_call('pg_dump --dbname={} > {}/backup_{}.bak'.format(
      options.psql_url,
      options.out_folder,
      datetime.now().strftime('%Y_%m_%d__%H_%M')))

    logging.info('Now let\'s sleep for a minute because I\'m to lazy '
                 + 'to fix infinite check_call calls which would happen '
                 + 'now because a minute has not passed yet')
    time.sleep(60)

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
