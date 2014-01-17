import requests
import urlparse

class Client(object):

    def __init__(self, base_uri=None):
        self.base_uri = base_uri
        self._session = None

    def set_basic_auth(self, user, password):
        self.session.auth = (user, password)

    def set_headers(self, headers):
        self.session.headers.update(headers)

    @property
    def session(self):
        if self._session is None:
            self._session = requests.Session()
        return self._session

    def fetch(self, request):
        if isinstance(request, basestring):
            joined = urlparse.urljoin(self.base_uri, request)
            return self.session.get(joined)
        elif isinstance(request, requests.Request):
            joined = urlparse.urljoin(self.base_uri, request.url)
            prepared = request.prepare()
            return self.session.send(prepared)
        else:
            raise TypeError('Request should be an instance of request.Request or a string')
