from .client import Client
client = Client()

from .resources import parties
Person = parties.Person
Persons = parties.Persons(client)
Parties = parties.Parties(client)

from .resources import history
HistoryItem = history.HistoryItem
History = history.History(client)

from .resources import cases
Case = cases.Case
Cases = cases.Cases(client)

from .resources import custom_fields
CustomField = custom_fields.CustomField
CustomFields = custom_fields.CustomFields(client)

from .resources import tags
Tag = tags.Tag
Tags = tags.Tags(client)
