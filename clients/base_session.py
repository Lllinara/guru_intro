import logging

from requests import Session

class BaseSession(Session):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.base_url = kwargs.get('base_url', None)

    def request(self, method, path, *args, **kwargs):
        url = self.base_url + path
        logging.info(url)
        return super().request(method, url, **kwargs)