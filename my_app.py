#!/usr/bin/env python3

import time

def log_time():
    while True:
        with open('logs/time.log', 'a') as log_file:
            log_file.write(time.strftime("%Y-%m-%d %H:%M:%S") + '\n')
        time.sleep(3)

while True:
    log_time()
