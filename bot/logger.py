from os import path
from datetime import datetime

LOG_FILE = './bot/logs.txt'

def current_time():
    return datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")

def add_post(log):
    log_file = open(LOG_FILE, 'a')
    log_file.write('[' + current_time() + '] ' + str(log) + '\n')
    log_file.close()

def get_log():
    log_file = open(LOG_FILE, 'r')
    log = log_file.readlines()
    log_file.close()
    return log
