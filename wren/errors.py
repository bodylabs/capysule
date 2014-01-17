class WrenError(Exception):
    pass


class HTTPError(WrenError):
    # def __init__(self, code):
        # if code == 599:
        #     message = 'Timeout'
        # else:
        #     message = httplib.responses[code]

        # super(HTTPError, self).__init__(message)
        # self.code = code
    pass
