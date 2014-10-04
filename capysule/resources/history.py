from booby import Model, fields
from booby.errors import ValidationError
from ..collection import Collection


class HistoryItem(Model):
    id = fields.Integer(primary=True)
    type = fields.String()
    subject = fields.String()
    note = fields.String()

    entry_date = fields.String(name='entryDate', read_only=True)
    creator = fields.String(read_only=True)
    creator_name = fields.String(read_only=True)

    party = None
    opportunity = None
    case = None

    @property
    def _url(self):
        if getattr(self, '_persisted', False) is True:
            return '/api/history/%s' % self.id
        if not (self.party or self.opportunity or self.case):
            raise ValidationError('Party, opportunity, or case is required')
        if bool(self.party) + bool(self.opportunity) + bool(self.case) > 1:
            raise ValidationError('Should only provide one of party, opportunity, case')
        if self.party:
            return '/api/party/%s/history' % self.party.id
        elif self.opportunity:
            return '/api/opportunity/%s/history' % self.opportunity.id
        elif self.case:
            return '/api/kase/%s/history' % self.case.id


class History(Collection):
    model = HistoryItem
    url = None

    def encode(self, obj):
        return {'historyItem': super(History, self).encode(obj)}
