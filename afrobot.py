#!/usr/bin/python
import os
import sys

from jobs.acc_stats import ACCStats
from utils.settings import Settings

__author__  = 'AfroThundr'
__license__ = "GNU GPLv3"
__title__   = 'AfroBot'
__version__ = "0.1.0"
__website__ = 'https://github.com/AfroThundr3007730/AfroBot'

class AfroBot(object):
    _id = 'afrobot'

    def __init__(self):
        # Function config
        with Settings() as self.settings:
            if not self.settings:
                self.settings = self._default
        return

    def __info__(self):
        # Return bot info
        return

    def run(self, *args, **kwargs):
        # The magic
        return

    _default = {
        '_schema_version': '1',
        'meta': {
            'author': str(__author__),
            'license': str(__license__),
            'name': str(__title__),
            'source': str(__website__),
            'version': str(__version__)
        },
        'sites': {
            'enwiki': {
                'name': 'English Wikipedia',
                'pass': 'CHANGEME',
                'uri': 'https://en.wikipedia.org/mediawiki/api.php',
                'user': 'MyBotUser'
            }
        },
        'tasks': {}
    }


def main():
    return


if __name__ == '__main__':
    main()
