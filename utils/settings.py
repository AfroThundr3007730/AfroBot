import io
import os

from box import Box

class Settings(object):
    _config_location = 'config.json'

    def __init__(self):
        if os.path.exists(self._config_location):
            self.__dict__ = Box.from_json(filename=self._config_location,
                                          box_it_up=True)
        else:
            self.__dict__ = Box()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self.__dict__.to_json(filename=self._config_location,
                              sort_keys=True, indent=4)
