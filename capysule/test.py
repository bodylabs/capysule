#!/usr/bin/env python

import os
import sys
# fix sys path so we don't need to setup PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def main():        
    from capysule.client import Client
    from capysule.resources import Parties, Person

    client = Client()

    parties = Parties(client)
    result = parties.all()
    print result[0]
    # print result[0].id

    # aaron = parties.get(52082372)
    # print aaron

    paul = parties.get(54607911)
    print paul

    new_contact = Person(first_name='Joe', last_name='Test')
    parties.add(new_contact)
    print new_contact
    print new_contact.id

if __name__ == '__main__':
    main()
