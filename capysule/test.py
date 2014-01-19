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

    paul = capysule.Parties.get(54607911)
    print paul

    new_contact = capysule.Person(first_name='Joe', last_name='Test')
    capysule.Parties.add(new_contact)
    print new_contact
    print new_contact.id

    history_item = capysule.HistoryItem(note='This is a note.')
    history_item.party = new_contact
    capysule.History.add(history_item)

    case = capysule.Case(name='New User')
    case.party = new_contact
    capysule.Cases.add(case)

    history_item = capysule.HistoryItem(note='User registered for BodyHub')
    history_item.case = case
    capysule.History.add(history_item)


if __name__ == '__main__':
    main()
