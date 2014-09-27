from booby import Model, fields
from booby.errors import ValidationError
from ..collection import Collection


class CustomField(Model):
    tag = fields.String()
    label = fields.String()
    string_value = fields.String(name='text')
    date_value = fields.String(name='date')
    boolean_value = fields.Boolean(name='boolean')

    party = None
    opportunity = None
    case = None

    @property
    def _url(self):
        if not (self.party or self.opportunity or self.case):
            raise ValidationError('Party, opportunity, or case is required')
        if bool(self.party) + bool(self.opportunity) + bool(self.case) > 1:
            raise ValidationError('Should only provide one of party, opportunity, case')
        if self.party:
            return '/api/party/%s/customfields' % self.party.id
        elif self.opportunity:
            return '/api/opportunity/%s/customfields' % self.opportunity.id
        elif self.case:
            return '/api/kase/%s/customfields' % self.case.id


class CustomFields(Collection):
    model = CustomField
    url = None

    def serialize(self, obj):
        return {'customFields': {'customField': super(CustomFields, self).serialize(obj)}}
