from booby import Model, fields
from booby.errors import ValidationError
from ..collection import Collection


class Tag(Model):
    name = fields.String()

    party = None
    opportunity = None
    case = None

    @property
    def _url(self):
        if not self.name:
            raise ValidationError('Tag name is required')
        if not (self.party or self.opportunity or self.case):
            raise ValidationError('Party, opportunity, or case is required')
        if bool(self.party) + bool(self.opportunity) + bool(self.case) > 1:
            raise ValidationError('Should only provide one of party, opportunity, case')
        if self.party:
            return '/api/party/%s/tag/%s' % (self.party.id, self.name)
        elif self.opportunity:
            return '/api/opportunity/%s/tag/%s' % (self.opportunity.id, self.name)
        elif self.case:
            return '/api/kase/%s/tag/%s' % (self.case.id, self.name)

    def __iter__(self):
        '''
        It's all in the URL.
        
        '''
        for k, v in {}:
            yield k, v

class Tags(Collection):
    model = Tag
    url = None

    def encode(self, obj):
        return {'tags': {'tag': super(Tags, self).encode(obj)}}
