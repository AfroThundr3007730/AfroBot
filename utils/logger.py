import os

from datetime import datetime as date

from utils.settings import Settings


class Logger(object):
    id = 'logger'

    def __init__(self, env='prod'):
        with Settings() as s:
            self.settings = s[self.id] = (
                self._default if not self.id in s else s[self.id])
        for f in 'debug_log', 'info_log', 'warn_log', 'error_log':
            self.settings[f + '_path'] = os.path.join(
                self.settings.logdir, env,
                self.settings[f] if f in self.settings else
                self.settings.default_log)

    def logdebug(self, message):
        self.log('DEBUG', message, log_file=self.settings.debug_log_path)

    def loginfo(self, message):
        self.log('INFO', message, log_file=self.settings.info_log_path)

    def logwarn(self, message):
        self.log('WARN', message, log_file=self.settings.warn_log_path)

    def logerror(self, message):
        self.log('ERROR', message, log_file=self.settings.error_log_path)

    @staticmethod
    def log(level, message, log_file=None):
        print('%s - %s: %s' %
              (date.now().replace(microsecond=0), level, message))
        print('Log file: %s' %
              (os.path.abspath(log_file) if log_file else None))
        if log_file and os.path.dirname(log_file) and not (
                os.path.exists(os.path.dirname(log_file))):
            os.makedirs(os.path.dirname(log_file), exist_ok=True)

    _default = {
        'logdir': 'logs',
        'default_log': 'main.log',
        'debug_log': 'debug.log',
        'error_log': 'error.log'
    }
