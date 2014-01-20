import os
from wren.client import Client as WrenClient

class Client(WrenClient):
    def __init__(self, site=None, api_token=None, **kwargs):
        if site is None:
            self.site = os.environ['CAPSULE_SITE']
        else:
            self.site = site
        if api_token is None:
            api_token = os.environ['CAPSULE_API_TOKEN']

        url = "https://%s.capsulecrm.com" % self.site
        super(Client, self).__init__(url, **kwargs)

        self.set_basic_auth(api_token, 'x')
        self.set_headers({'Accept': 'application/json'})
