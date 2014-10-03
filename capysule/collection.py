import os
from wren.collection import Collection as WrenCollection

class NotFound(Exception):
    pass

class Collection(WrenCollection):
    def handle_error(self, response):
        import requests
        if response.status_code == requests.codes.not_found and response.json() == {'message': 'Could not find resource'}:
                raise NotFound(response.text)
        else:
            super(Collection, self).handle_error(response)
