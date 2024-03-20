#!/usr/bin/python
import os

from utils.loader import TaskLoader
from utils.logger import Logger
from utils.settings import Settings

# To be replaced with dynamic plugin import
from jobs.acc_stats import ACCStats

__title__ = 'AfroBot Wikibot'
__version__ = '0.1.0'
__author__ = 'AfroThundr'
__license__ = 'GNU GPLv3'
__source__ = 'https://github.com/AfroThundr3007730/AfroBot'


class AfroBot(object):
    id = 'afrobot'
    env = os.environ['BOT_MODE'] if 'BOT_MODE' in os.environ else 'dev'
    L = Logger(env)

    def __init__(self):
        with Settings() as self.settings:
            if not self.settings:
                L.logwarn('No settings detected, populating defaults.')
                self.settings = self._default
            self.settings.meta = self._meta
        L.loginfo('Settings loaded successfully.')

    def _info(self):
        # Put some proper info here
        print('%s' (_meta))

    def runs(self, *args, **kwargs):
        # The magic
        L.loginfo('Starting %s (version %s).' % (__title__, __version__))
        L.loginfo('Loading all task plugins.')
        TaskLoader.loadall()

    def run(self):
        print('hello world')

    _meta = {
        'author':  __author__,
        'botname': __title__,
        'license': __license__,
        'source':  __source__,
        'version': __version__
    }

    _default = {
        '_schema_version': __version__,
        'meta': _meta,
        'sites': {
            'enwiki': {
                'name': 'English Wikipedia',
                'pass': 'CHANGEME',
                'uri':  'https://en.wikipedia.org/mediawiki/api.php',
                'user': 'MyBotUser'
            }
        },
        'tasks': {}
    }


if __name__ == '__main__':
    AfroBot().run()
