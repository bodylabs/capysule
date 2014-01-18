#!/usr/bin/env python

import os
import sys
# fix sys path so we don't need to setup PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def main():
    import capysule
    result = capysule.Parties.all()
    print result[0]
    print result[0].id

    # aaron = parties.get(52082372)
    # print aaron

    paul = capysule.Parties.get(54607911)
    print paul

    new_contact = capysule.Person(first_name='Joe', last_name='Test')
    capysule.Parties.add(new_contact)
    print new_contact
    print new_contact.id

if __name__ == '__main__':
    main()
