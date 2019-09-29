import os

from box import Box, BoxList


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

    def __exit__(self, type, value, traceback):
        self.__dict__.to_json(filename=self._config_location,
                              sort_keys=True, indent=4)

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        if type(value) is list:
            return setattr(self, key, BoxList(value))
        elif type(value) is dict:
            return setattr(self, key, Box(value))
        else:
            return setattr(self, key, value)

    def __delitem__(self, key):
        return delattr(self, key)

    def __repr__(self):
        return repr(self.__dict__)

    def save(self):
        return self.__exit__(None, None, None)
