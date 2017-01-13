import time
import sys

class Observer:
    def __init__(self, url: str, email: str = None, interval: int = 5*60):
        self.url = url
        self.email = email

        if interval >= 5:
            self.interval = interval
        else:
            raise ValueError("Can't fetch that regularly.")

    def notify(self):
        if self.email:
            pass
        else:
            raise ValueError("Email is missing")

    def fetch(self):
        print("Fetching...")

    def run(self):
        try:
            while True:
                self.fetch()
                time.sleep(self.interval)
                
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit()