import xml
from datetime import datetime as date

import mwparserfromhell as parser
import requests
from bs4 import BeautifulSoup as bs

from utils.settings import Settings


class ACCStats(object):
    id = 'acc_stats'

    def __init__(self):
        with Settings() as s:
            self.settings = s.tasks[self.id] = (
                self._default if not self.id in s.tasks else s.tasks[self.id])
        self.stats={}

    def _info(self):
        # Return task info
        if not self.start_time:
            self.start_time = date.now()
        if not self.edit_count:
            self.edit_count = 0

    def run(self, *args, **kwargs):
        # The magic
        return

    _default = {
        'config': {
            'acc_uri': 'https://accounts.wmflabs.org/api.php',
            'prod': 'enwiki',
            'sites': {
                'enwiki': {
                    'flag': 'no',
                    'page': 'User:AfroBot/accstats',
                    'rate': 'hourly',
                    'summary': 'Updating [[WP:ACC|ACC]] request statistics.'
                }
            }
        },
        'desc': 'Updates WP:ACC Statistics on enwiki',
        'name': 'ACC Statistics',
        'status': 'active'
    }
