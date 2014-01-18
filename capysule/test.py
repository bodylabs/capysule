#!/usr/bin/env python

import os
import sys
# fix sys path so we don't need to setup PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def main():        
    from wren.client import Client
    from capysule.resources import Parties

    client = Client('https://bodylabs.capsulecrm.com')
    client.set_basic_auth(os.environ['CAPSULE_API_TOKEN'], 'x')
    client.set_headers({'Accept': 'application/json'})

    parties = Parties(client)
    result = parties.all()
    print result[0]
    print result[0].id

    aaron = parties.get(52082372)
    print aaron

if __name__ == '__main__':
    main()
