import constants
import requests
import time
import sys

class Observer:
    def __init__(self, url, email = None, interval = 5*60):
        self.url = url
        self.email = email

        if interval >= 5:
            self.interval = interval
        else:
            raise ValueError(constants.FETCH_INTERVAL_ERROR)

    def notify(self):
        if self.email:
            pass
        else:
            raise ValueError(constants.MISSING_EMAIL_ERROR)

    def fetch(self):
        print(constants.FETCH)

    def run(self):
        try:
            while True:
                self.fetch()
                time.sleep(self.interval)
                
        except KeyboardInterrupt:
            print(constants.EXIT)
            sys.exit()