import os

from importlib import import_module, reload

from utils.settings import Settings


class TaskLoader(object):
    id = 'loader'

    def __init__(self, autoload=True):
        with Settings() as s:
            self.settings = s[self.id] = (
                self._default if not self.id in s else s[self.id])

    def loadall(self):
        return

    def load(self, task):
        return

    _default = {
        'taskdir': 'tasks'
    }
