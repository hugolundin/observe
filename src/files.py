from lxml.etree import tostring
from lxml import html
import constants
import requests
import datetime

class Files:
    @staticmethod
    def download(url):
        print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {constants.DOWNLOAD}")
        page = requests.get(url)
        return tostring(html.fromstring(page.content))

    @staticmethod
    def compare(base_version, new_version):
        return base_version == new_version