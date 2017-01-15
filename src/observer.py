from filecmp import dircmp
import constants
import requests
import error

class Observer:
    def __init__(self, url, email = None, interval=constants.DEFAULT_INTERVAL):
        self.url = url
        self.email = email

        if interval >= constants.MIN_INTERVAL:
            self.interval = interval
        else:
            raise error.IntervalError(constants.FETCH_INTERVAL_ERROR)

    def notify(self):
        if self.email:
            print("Email sent")
        else:
            raise error.EmailError(constants.MISSING_EMAIL_ERROR)
