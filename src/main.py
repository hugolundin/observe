import observer
from files import Files
import constants
import datetime
import click
import error
import time
import sys

@click.command()
@click.argument('url')
@click.option('--email',    help=constants.EMAIL_HELP)
@click.option('--interval', help=constants.INTERVAL_HELP,
                            default=constants.DEFAULT_INTERVAL)

def main(url, email, interval):
    try:
        current = observer.Observer(url, email, interval)

        try:
            base = Files.download(current.url)
            time.sleep(current.interval)

            while True:
                new = Files.download(current.url)

                if not Files.compare(base, new):
                    # TODO: Notify user by sending email
                    print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {constants.CHANGES}")
                    base = new

                time.sleep(current.interval)

        except KeyboardInterrupt:
            print(constants.EXIT)
            sys.exit()

    except error.IntervalError:
        print(DOWNLOAD_INTERVAL_ERROR)
        sys.exit()

if __name__ == '__main__':
    main()
    
